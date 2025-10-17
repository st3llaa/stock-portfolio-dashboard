# Stock Portfolio Analyzer is a data-driven web dashboard built with Python + Streamlit: # 
- Takes user input (stock tickers and portfolio weights)
- Pulls real-time market data for those stocks from Yahoo Finance
- Computes portfolio metrics, such as:
- Daily & annualized returns
- Portfolio volatility
- Sharpe Ratio (risk-adjusted performance)
- Displays the results visually in an interactive dashboard (charts & metrics)

## How to Run... #
`git clone https://github.com/st3llaa/stock-portfolio-dashboard.git
cd stock-portfolio-dashboard
pip install -r requirements.txt
streamlit run app.py`

## Next steps... #
Use Alpha Vantage API to add:

- RSI (Relative Strength Index)
- MACD (Momentum indicator)
- Bollinger Bands

Use Firebase or Supabase to let users save their portfolios and revisit later.

once ready to deploy: https://share.streamlit.io/