# AI Trading Bot

## Overview

MLTrader is an algorithmic trading strategy implemented using the Lumibot framework. The strategy combines technical indicators, such as RSI (Relative Strength Index), with AI-driven sentiment analysis to make informed trading decisions. It operates on a list of specified symbols from the S&P 500, executing trades based on market conditions and news sentiment.



## Technologies

  #### Programming Languages: 
    Python
  #### Libraries:
    Lumibot
    Alpaca API
    pandas
    transformers
    torch
    ta
  #### Tools:
    Alpaca Paper Trading
    Yahoo Finance

## APIs

  #### Alpaca Trade REST API: 
  Utilized for executing trades, fetching news, and accessing market data. It is accessed through the alpaca_trade_api.REST client and the Alpaca class from lumibot.brokers. 

  #### Yahoo Finance Data:
  Used for backtesting your strategy using historical market data from Yahoo Finance.

 #### FinBERT on Hugging Face:
  Sentiment analysis model used to estimate sentiment from news headlines.

## Features

  #### Technical Analysis: 
  Utilizes the RSI (Relative Strength Index) to identify potential buy and sell signals.
  #### Sentiment Analysis: 
  Implements AI-driven sentiment analysis using the FinBERT model to gauge market sentiment from news headlines.
  #### Automated Trading: 
  Executes trades based on combined signals from RSI and sentiment analysis.
  #### Backtesting: 
  Supports backtesting with historical data from Yahoo Finance to evaluate strategy performance before live trading.
  #### Risk Management: 
  Includes risk management features such as setting cash at risk and using bracket orders for take-profit and stop-loss.
