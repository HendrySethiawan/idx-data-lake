#!/usr/bin/env python3
"""IDX Real-Time Data Lake - Production Pipeline Entry Point"""

import logging
import sys
from datetime import datetime
from config.settings import settings
from config.database import init_db
from src.ingestion.yfinance_fetcher import IDXDataIngestor
from src.transformation.feature_engineer import IDXFeatureEngineer
from src.storage.data_lake import store_batch
from src.monitoring.quality_monitor import DataQualityMonitor
from src.api.app import app
import uvicorn

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("pipeline")

def run_pipeline():
    logger.info("="*60)
    logger.info("IDX DATA LAKE PIPELINE STARTED")
    logger.info("="*60)
    
    start = datetime.now()
    
    try:
        # 1. Init DB
        logger.info("[1/5] Initializing database & TimescaleDB...")
        init_db()
        
        # 2. Ingest
        logger.info("[2/5] Fetching market data...")
        ingestor = IDXDataIngestor(settings.TICKERS)
        raw_data = ingestor.fetch()
        
        # 3. Transform
        logger.info("[3/5] Engineering features...")
        transformer = IDXFeatureEngineer()
        transformed = transformer.process_batch(raw_data)
        
        # 4. Validate
        logger.info("[4/5] Running data quality checks...")
        monitor = DataQualityMonitor()
        metrics = monitor.validate(transformed)
        
        for ticker, m in metrics.items():
            logger.info(f"  {ticker}: {m['records']} records | {m['completeness_pct']}% complete | {m['status']}")
            
        # 5. Store
        logger.info("[5/5] Storing to TimescaleDB...")
        stored = store_batch(transformed)
        logger.info(f"Successfully stored {stored} datasets.")
        
        elapsed = (datetime.now() - start).total_seconds()
        logger.info(f"✅ PIPELINE COMPLETED IN {elapsed:.2f}s")
        
    except Exception as e:
        logger.error(f"❌ Pipeline failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="IDX Data Lake Pipeline")
    parser.add_argument("--api", action="store_true", help="Run FastAPI server instead of pipeline")
    args = parser.parse_args()
    
    if args.api:
        logger.info("Starting FastAPI server on port 8000...")
        uvicorn.run("src.api.app:app", host="127.0.0.1", port=8000, reload=True)
    else:
        run_pipeline()
