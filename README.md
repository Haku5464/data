# Apple Inc Financial Analysis Dashboard

## Introduction

This is a financial analysis dashboard for Apple Inc. The dashboard is built using Streamlit, a Python framework for building analytical web applications. 

## Data

The financial data is collected manually from Apple Inc's [Investor Relations](https://investor.apple.com/stock-price/default.aspx) page. The data is stored in a CSV file.

## Quickstart

## Local run

### Install dependencies

```shell
pip install -r requirements.txt
```

### Run service

```shell
streamlit run app.py
```

## Docker run

### Docker build

```shell
# Image build
docker build -t apple-financial-analysis-dashboard .
# Run service in container
docker run -p 8501:8501 apple-financial-analysis-dashboard
```

### Google Cloud Service

```shell
# Image build
gcloud builds submit --tag gcr.io/circus-399407/apple-financial-analysis-dashboard
```