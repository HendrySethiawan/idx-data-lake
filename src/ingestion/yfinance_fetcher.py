import yfinance as yf
import pandas as pd
from typing import Dict, List, Optional
import time
import logging

logger = logging.getLogger(__name__)

class IDXDataIngestor:
    def __init__(self, tickers: List[str]):
        self.tickers = tickers

    def fetch(self) -> Dict[str, pd.DataFrame]:
        data_dict = {}
        for i, ticker in enumerate(self.tickers):
            try:
                if i > 0:
                    time.sleep(0.5)  # Rate limiting
                logger.info(f"Fetching {ticker}...")
                
                df = yf.download(
                    tickers=ticker,
                    period="2y",
                    interval="1d",
                    progress=False
                )
                
                if df.empty:
                    logger.warning(f"No data returned for {ticker}")
                    continue
                    
                df['ticker'] = ticker
                df['source'] = 'yfinance'
                df['last_updated'] = pd.Timestamp.now()
                df.index.name = 'time'
                
                data_dict[ticker] = df
            except Exception as e:
                logger.error(f"Failed to fetch {ticker}: {e}")
                
        return data_dict
