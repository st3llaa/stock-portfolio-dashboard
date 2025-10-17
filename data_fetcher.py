import yfinance as yf
import pandas as pd
import os
from dotenv import load_dotenv
from alpha_vantage.techindicators import TechIndicators

# Load environment variables from .env file (API key)
load_dotenv()
api_key = os.getenv("ALPHA_VANTAGE_KEY")

def get_stock_data(tickers, period='1y'):
    """
    Fetch historical price data for multiple tickers.
    """
    data = yf.download(tickers, period=period)['Close']
    if isinstance(data, pd.Series):  # Only one ticker
        data = data.to_frame()
    return data

def get_benchmark_data(symbol="SPY", start=None, end=None):
    benchmark = yf.download(symbol, start=start, end=end)["Close"]
    return benchmark

def get_rsi(symbol, interval='daily', time_period=14):
    ti = TechIndicators(key=api_key, output_format='pandas')
    rsi, _ = ti.get_rsi(symbol=symbol, interval=interval, time_period=time_period)
    return rsi

def get_macd(symbol, interval='daily'):
    ti = TechIndicators(key=api_key, output_format='pandas')
    macd, _ = ti.get_macd(symbol=symbol, interval=interval, series_type='close')
    return macd

def get_bollinger_bands(symbol, interval='daily', time_period=20):
    ti = TechIndicators(key=api_key, output_format='pandas')
    bb, _ = ti.get_bbands(symbol=symbol, interval=interval, time_period=time_period,
                          series_type='close', nbdevup=2, nbdevdn=2)
    return bb


