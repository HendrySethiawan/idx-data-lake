# IDX Real-Time Data Lake - Production

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![Status](https://img.shields.io/badge/Status-Production_Ready-brightgreen.svg)

A production-grade, Dockerized pipeline for Indonesian equity market analytics. Fuses electrical engineering signal processing with quantitative finance to build a defensible, institutional-grade data infrastructure.

## 📖 Overview
This system ingests IDX market data, applies EE-inspired signal processing (wavelets, Kalman filtering, control-theory corrections), validates data quality, and stores results in a TimescaleDB time-series database. It exposes a FastAPI REST layer for downstream quant models, prop-trading desks, and fintech integrations.

## 🏗️ Architecture
```
[Data Source] → [Ingestion] → [Transformation] → [Storage] → [Serving]
         ↓             ↓              ↓            ↓           ↓
    yfinance     Technical       PostgreSQL   FastAPI      Monitoring  
     (OHLCV)    Indicators     + TimescaleDB  REST APIs     Validation
```

## ✨ Key Features
- ✅ EE-inspired feature engineering (wavelet decomposition, Kalman smoothing, PID error correction)
- ✅ TimescaleDB hypertables optimized for high-frequency time-series
- ✅ Automated data quality validation & pipeline latency tracking
- ✅ FastAPI REST endpoints with health checks, summary endpoints, and auto-generated docs
- ✅ Dockerized infrastructure (PostgreSQL, Redis, MinIO) with zero host dependencies
- ✅ Modular, type-safe, production-ready codebase following PEP 8 & quant engineering standards

## 🚀 Quick Start

### Prerequisites
- Docker Desktop (WSL2 backend enabled)
- Python 3.11+ with `venv`
- Git

### 1. Clone & Configure
```cmd
git clone <your-repo-url>
cd idx_data_lake_prod
copy .env.example .env
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Start Infrastructure
```cmd
docker compose up -d db redis minio
```

### 3. Run Pipeline
```cmd
python main.py
```

### 4. Start API Server
```cmd
python main.py --api
# Access interactive docs: http://127.0.0.1:8000/docs
```

## ⚙️ Configuration
All runtime settings are managed via `.env`. Copy `.env.example` to `.env` and adjust as needed:
```env
DB_HOST=db
DB_PORT=5432
DB_NAME=idx_data
DB_USER=postgres
DB_PASSWORD=password
REDIS_HOST=redis
REDIS_PORT=6379
MINIO_ENDPOINT=http://minio:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_BUCKET=idx-data-lake
PIPELINE_INTERVAL_MINUTES=15
MAX_RETRY_ATTEMPTS=3
DATA_RETENTION_DAYS=730
```

## 📁 Project Structure
```
idx_data_lake_prod/
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── main.py
├── config/
│   ├── settings.py          # Pydantic configuration
│   └── database.py          # SQLAlchemy engine & session
├── src/
│   ├── ingestion/           # yfinance data fetcher
│   ├── transformation/      # Technical & EE feature engineering
│   ├── storage/             # TimescaleDB hypertable manager
│   ├── monitoring/          # Quality validation & metrics
│   └── api/                 # FastAPI server & routes
├── tests/
└── README.md
```

## 🔌 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/`      | Root status & version |
| `GET`  | `/health`| Service health check |
| `GET`  | `/data/summary` | Pipeline config & ticker list |
| `GET`  | `/docs`  | Auto-generated FastAPI Swagger UI |

## 📊 Monitoring & Validation
- **Pipeline Latency**: Tracked & logged per execution cycle
- **Data Completeness**: Validates >99% record integrity across LQ45 tickers
- **Health Checks**: Docker-native `pg_isready`, `redis-cli ping`, MinIO `/minio/health/live`
- **Structured Logging**: `logging` module with timestamps, levels, and component tags
- **Error Handling**: Graceful fallbacks, retry limits, and non-blocking pipeline continuation

## 🚀 Next Steps
1. **Fundamental + Technical Screener**: Build Streamlit dashboard with XGBoost undervaluation ranking & FFT momentum filters
2. **Time-Series Forecasting Engine**: Deploy PyTorch LSTM/Transformer models with wavelet-decomposed inputs & PID error correction
3. **Indonesian Sentiment Alpha Pipeline**: Fine-tune IndoBERT on ID-SMSA + local news scraping for mean-reversion signals
4. **Statistical Arbitrage & Pairs Trading Bot**: Implement Engle-Granger cointegration + Kalman-filtered spread trading
5. **Reinforcement-Learning Portfolio Optimizer**: Train PPO/DQN agents for dynamic sector allocation with transaction cost & FX hedging
6. **Anomaly Detection for Market Surveillance**: Autoencoder + isolation forest for flash-crash precursor detection
7. **Career Monetization**: Package track record for prop desks, fintech quant roles, or OJK-licensed seed fund

## 🤝 Contributing
Contributions are welcome and encouraged. Please follow these guidelines:
- Fork the repository and create a feature branch (`feature/<description>`)
- Follow PEP 8 and format code with `black`
- Add unit tests for new components in `tests/`
- Ensure all Docker services remain healthy (`docker compose up -d`)
- Submit a PR with a clear description of changes, testing steps, and expected outcomes
- Do not commit `.env`, credentials, or large binary files

## 📬 Contact
- **Email**: [your.email@example.com]
- **LinkedIn**: [linkedin.com/in/yourprofile]
- **GitHub**: [github.com/yourusername]
- **Professional Blog/Portfolio**: [yourwebsite.com]
For collaboration, quant strategies, or prop-firm partnerships, please reach out via email or LinkedIn.

## 📜 License
MIT
```
