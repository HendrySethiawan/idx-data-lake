import pandas as pd
import numpy as np
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class IDXFeatureEngineer:
    def __init__(self):
        pass

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df = df.ffill().bfill()
        df = df[~df.index.duplicated(keep='first')]
        return df

    def add_technicals(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        # Moving Averages
        if len(df) >= 5:
            df['MA_5'] = df['Close'].rolling(5, min_periods=1).mean()
        if len(df) >= 20:
            df['MA_20'] = df['Close'].rolling(20, min_periods=1).mean()
            
        # RSI
        if len(df) >= 14:
            delta = df['Close'].diff()
            gain = delta.where(delta > 0, 0).rolling(14, min_periods=1).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(14, min_periods=1).mean()
            rs = gain / loss.replace(0, np.nan)
            df['RSI'] = 100 - (100 / (1 + rs))
            
        # Bollinger Bands
        if len(df) >= 20:
            bb_mid = df['Close'].rolling(20, min_periods=1).mean()
            bb_std = df['Close'].rolling(20, min_periods=1).std()
            df['BB_Middle'] = bb_mid
            df['BB_Upper'] = bb_mid + (bb_std * 2)
            df['BB_Lower'] = bb_mid - (bb_std * 2)
            
        # Volume Ratio (safe division)
        if len(df) >= 10:
            vol_ma = df['Volume'].rolling(10, min_periods=1).mean()
            df['Volume_Ratio'] = np.where(vol_ma > 0, df['Volume'] / vol_ma, np.nan)
            
        # Price features
        df['Price_Change_Pct'] = df['Close'].pct_change()
        df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
        
        # EE-inspired volatility proxy
        if len(df) >= 20:
            df['Volatility_20d'] = df['Close'].rolling(20, min_periods=1).std()
            
        return df

    def process_batch(self, raw_data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
        transformed = {}
        for ticker, df in raw_data.items():
            if df.empty:
                continue
            try:
                cleaned = self.clean(df)
                featured = self.add_technicals(cleaned)
                transformed[ticker] = featured
            except Exception as e:
                logger.error(f"Transformation failed for {ticker}: {e}")
        return transformed
