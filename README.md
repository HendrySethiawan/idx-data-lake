# IDX Data Lake - Skeleton Implementation

![Jupyter](https://img.shields.io/badge/Jupyter-%23F37600.svg?logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Skeleton%20Code-yellow.svg)

A lightweight, educational notebook for prototyping an Indonesian stock market data pipeline. Designed for rapid experimentation, signal exploration, and learning before scaling to production.

## 🎯 Purpose
- Demonstrate end-to-end data ingestion, transformation, and storage logic
- Integrate Electrical Engineering concepts (wavelets, Kalman filtering, control theory) into financial time-series
- Provide a reproducible foundation for quantitative research

## 🛠️ Setup
```cmd
cd idx-data-lake-skeleton
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 📖 Usage
1. Open `IDX_Data_Lake_Skeleton.ipynb` in VS Code or Jupyter
2. Run cells sequentially
3. Explore outputs: data frames, technical indicators, quality metrics, and storage logs
4. Modify tickers, parameters, or feature logic to experiment

## 📦 Dependencies
- `yfinance`, `pandas`, `numpy`, `sqlalchemy`, `psycopg2-binary`, `PyWavelets`, `great-expectations`
