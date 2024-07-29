# AI Trading Algorithm

Goal: 
  The goal of this project is to create a trading algorithm which uses AI to efficiently perform stock trades.
  To determine the success of this project, we will compare our trade profits against the S&P 500 (SPY). We are 
  using Alpaca trading API to make paper trades.


Stock is bought when the senitment of news received of a stock is positive and the probability of the sentiment being correct is 0.85 or greater.

Stock is sold when the sentiment is negative or if the stock has hit a stop-loss of 80% less than the original price. 

## APIs used:

  Alpaca Trade API: 
    This is used for executing trades, fetching news, and accessing market data. It is accessed through the alpaca_trade_api.REST client and the Alpaca class from lumibot.brokers. 

  Yahoo Finance Data:
    YahooDataBacktesting: This is used for backtesting your strategy using historical market data from Yahoo Finance.
