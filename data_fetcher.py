import yfinance as yf
import pandas as pd

def get_stock_data(tickers, period='1y'):
    """
    Fetch historical price data for multiple tickers.
    """
    data = yf.download(tickers, period=period)['Close']
    if isinstance(data, pd.Series):  # Only one ticker
        data = data.to_frame()
    return data
