import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf 
from data_fetcher import get_stock_data
from data_fetcher import get_benchmark_data
from portfolio_analysis import calculate_portfolio_returns, calculate_sharpe_ratio, moving_average
from portfolio_analysis import calculate_beta

st.set_page_config(page_title="Stock Portfolio Dashboard", layout="wide")

st.title("📈 Stock Portfolio Analyzer")

tickers = st.text_input("Enter stock tickers (comma-separated):", "AAPL, MSFT, TSLA")
weights_input = st.text_input("Enter portfolio weights (comma-separated):", "0.4, 0.4, 0.2")
#st.download_button("Download CSV", portfolio_returns.to_csv(), "portfolio.csv")


# Compute benchmark daily returns
benchmark_returns = benchmark.pct_change().dropna()
# Align portfolio and benchmark returns
aligned = pd.concat([portfolio_returns, benchmark_returns], axis=1).dropna()
aligned.columns = ["Portfolio", "SPY"]
# Covariance between portfolio and SPY, and variance of SPY
cov = aligned["Portfolio"].cov(aligned["SPY"])
var = aligned["SPY"].var()
beta = cov / var


if st.button("Analyze Portfolio"):
    # Parse user input
    tickers = [t.strip().upper() for t in tickers.split(",")]
    weights = np.array([float(w) for w in weights_input.split(",")])
    weights = weights / np.sum(weights)

    st.write("Fetching stock data...")
    prices = get_stock_data(tickers)

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
