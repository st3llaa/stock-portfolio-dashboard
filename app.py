import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf 
import time
from data_fetcher import get_stock_data, get_benchmark_data, get_rsi, get_macd, get_bollinger_bands
from portfolio_analysis import calculate_portfolio_returns, calculate_sharpe_ratio, moving_average, calculate_beta

st.set_page_config(page_title="Stock Portfolio Dashboard", layout="wide")

st.title("Stock Portfolio Analyzer 📈 ")

tickers = st.text_input("Enter stock tickers (comma-separated):", "AAPL, MSFT, TSLA")
weights_input = st.text_input("Enter portfolio weights (comma-separated):", "0.4, 0.4, 0.2")
#st.download_button("Download CSV", portfolio_returns.to_csv(), "portfolio.csv")


if st.button("Analyze Portfolio"):
    # Parse user input
    tickers = [t.strip().upper() for t in tickers.split(",")]
    weights = np.array([float(w) for w in weights_input.split(",")])
    weights = weights / np.sum(weights)

    st.write("Fetching stock data...")
    prices = get_stock_data(tickers)
    symbol = "AAPL"

    st.write("Calculating metrics...")
    portfolio_returns = calculate_portfolio_returns(prices, weights)
    sharpe_ratio = calculate_sharpe_ratio(portfolio_returns)

    # --- Fetch benchmark and calculate beta ---
    benchmark_prices = get_benchmark_data(start=prices.index.min(), end=prices.index.max())
    benchmark_returns = benchmark_prices.pct_change().dropna()
    beta_value = calculate_beta(portfolio_returns, benchmark_returns)
    # -------------------------------------------

    # Display metrics
    st.subheader("Portfolio Metrics")
    st.write(f"**Sharpe Ratio:** {sharpe_ratio:.2f}")
    st.write(f"**Average Annual Return:** {(portfolio_returns.mean() * 252) * 100:.2f}%")
    st.write(f"**Volatility:** {(portfolio_returns.std() * np.sqrt(252)) * 100:.2f}%")
    st.write(f"**Beta:** {beta_value:.2f}")
    
    # Charts
    st.subheader("Price Charts")
    st.line_chart(prices)

    st.subheader("Moving Averages (20-day)")
    st.line_chart(moving_average(prices))

    # Technical Indicators
    st.subheader(f"RSI for {symbol}")
    rsi = get_rsi(symbol)
    time.sleep(12) # Handle API rate limits
    st.line_chart(rsi)
    st.subheader(f"MACD for {symbol}")
    time.sleep(12) # Handle API rate limits
    macd = get_macd(symbol)
    st.line_chart(macd[['MACD', 'MACD_Signal']])
    st.subheader(f"Bollinger Bands for {symbol}")
    time.sleep(12) # Handle API rate limits
    bb = get_bollinger_bands(symbol)

    st.line_chart(bb)

    st.write("RSI Data Preview:", rsi.head())
    st.write("MACD Data Preview:", macd.head())
    st.write("BB Data Preview:", bb.head()) 