from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "idx_data"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password"
    
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    MINIO_ENDPOINT: str = "http://localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_BUCKET: str = "idx-data-lake"
    
    PIPELINE_INTERVAL_MINUTES: int = 15
    MAX_RETRY_ATTEMPTS: int = 3
    DATA_RETENTION_DAYS: int = 730
    
    TICKERS: List[str] = ["BBCA.JK", "TLKM.JK", "ASII.JK", "^JKSE"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

    @property
    def database_url(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()
