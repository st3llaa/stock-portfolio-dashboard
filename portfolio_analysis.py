import numpy as np
import pandas as pd

def calculate_portfolio_returns(prices, weights):
    returns = prices.pct_change().dropna()
    weighted_returns = returns.dot(weights)
    return weighted_returns

def calculate_sharpe_ratio(returns, risk_free_rate=0.03):
    excess_return = returns.mean() * 252 - risk_free_rate
    volatility = returns.std() * np.sqrt(252)
    return excess_return / volatility

def moving_average(prices, window=20):
    return prices.rolling(window=window).mean()

def calculate_beta(portfolio_returns, benchmark_returns):
    # Calculate beta of a portfolio vs a benchmark
    aligned = pd.concat([portfolio_returns, benchmark_returns], axis=1).dropna()
    aligned.columns = ["Portfolio", "Benchmark"]
    cov = aligned["Portfolio"].cov(aligned["Benchmark"])
    var = aligned["Benchmark"].var()
    beta = cov / var
    return beta

