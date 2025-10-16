import streamlit as st
import pandas as pd
import numpy as np
from data_fetcher import get_stock_data
from portfolio_analysis import calculate_portfolio_returns, calculate_sharpe_ratio, moving_average

st.set_page_config(page_title="Stock Portfolio Dashboard", layout="wide")

st.title("📈 Stock Portfolio Analyzer")

tickers = st.text_input("Enter stock tickers (comma-separated):", "AAPL, MSFT, TSLA")
weights_input = st.text_input("Enter portfolio weights (comma-separated):", "0.4, 0.4, 0.2")

if st.button("Analyze Portfolio"):
    tickers = [t.strip().upper() for t in tickers.split(",")]
    weights = np.array([float(w) for w in weights_input.split(",")])
    weights = weights / np.sum(weights)

    st.write("Fetching stock data...")
    prices = get_stock_data(tickers)

    st.write("Calculating metrics...")
    portfolio_returns = calculate_portfolio_returns(prices, weights)
    sharpe_ratio = calculate_sharpe_ratio(portfolio_returns)

    st.subheader("Portfolio Metrics")
    st.write(f"**Sharpe Ratio:** {sharpe_ratio:.2f}")
    st.write(f"**Average Annual Return:** {(portfolio_returns.mean() * 252) * 100:.2f}%")
    st.write(f"**Volatility:** {(portfolio_returns.std() * np.sqrt(252)) * 100:.2f}%")

    st.subheader("Price Charts")
    st.line_chart(prices)

    st.subheader("Moving Averages (20-day)")
    st.line_chart(moving_average(prices))
