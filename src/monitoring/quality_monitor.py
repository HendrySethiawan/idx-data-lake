import pandas as pd
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class DataQualityMonitor:
    def validate(self, data_dict: Dict[str, pd.DataFrame]) -> Dict[str, dict]:
        metrics = {}
        for ticker, df in data_dict.items():
            if df.empty:
                metrics[ticker] = {"status": "empty", "records": 0}
                continue
                
            total = len(df) * len(df.columns)
            missing = df.isnull().sum().sum()
            completeness = round((1 - missing/total) * 100, 2) if total > 0 else 0
            
            metrics[ticker] = {
                "records": total,
                "missing_values": int(missing),
                "completeness_pct": completeness,
                "status": "pass" if completeness >= 99.0 else "warning"
            }
        return metrics
