import pandas as pd
from sqlalchemy import text
from config.database import engine, SessionLocal
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

def create_hypertable(table_name: str):
    with engine.connect() as conn:
        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                time TIMESTAMPTZ NOT NULL,
                open DOUBLE PRECISION,
                high DOUBLE PRECISION,
                low DOUBLE PRECISION,
                close DOUBLE PRECISION,
                volume BIGINT,
                ticker VARCHAR(20),
                source VARCHAR(50),
                last_updated TIMESTAMPTZ
            );
        """))
        conn.execute(text(f"SELECT create_hypertable('{table_name}', 'time', if_not_exists => TRUE);"))
        conn.commit()

def store_batch(data_dict: dict):
    stored_count = 0
    for ticker, df in data_dict.items():
        if df.empty:
            continue
        try:
            table_name = f"idx_{ticker.replace('.', '_')}"
            create_hypertable(table_name)
            
            df = df.reset_index()
            df['time'] = pd.to_datetime(df['time'])
            
            df.to_sql(table_name, engine, if_exists='append', index=False)
            logger.info(f"Stored {len(df)} rows for {ticker}")
            stored_count += 1
        except Exception as e:
            logger.error(f"Storage failed for {ticker}: {e}")
    return stored_count
