from fastapi import FastAPI
from config.settings import settings
import logging

logger = logging.getLogger(__name__)
app = FastAPI(title="IDX Real-Time Data Lake", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "IDX Data Lake API is operational"}

@app.get("/health")
async def health():
    return {"status": "healthy", "tickers_count": len(settings.TICKERS)}

@app.get("/data/summary")
async def summary():
    return {
        "tickers": settings.TICKERS,
        "pipeline_interval_minutes": settings.PIPELINE_INTERVAL_MINUTES,
        "retention_days": settings.DATA_RETENTION_DAYS
    }
