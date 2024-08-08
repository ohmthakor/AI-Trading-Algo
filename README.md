# AI Trading Bot

## Overview

MLTrader is an algorithmic trading strategy implemented using the Lumibot framework. The strategy combines technical indicators, such as RSI (Relative Strength Index), with AI-driven sentiment analysis to make informed trading decisions. It operates on a list of specified symbols from the S&P 500, executing trades based on market conditions and news sentiment.



## Technologies

**Programming Languages**:
    Python
**Libraries**:
  - [Lumibot](https://github.com/Lumibot/lumibot)
  - [Alpaca](https://alpaca.markets/) API
  - [pandas](https://pandas.pydata.org/)
  - [transformers](https://huggingface.co/transformers/)
  - [torch](https://pytorch.org/)
  - [ta](https://github.com/bukosabino/ta)
**Tools**:
  - [Alpaca Paper Trading](https://alpaca.markets/docs/trading-on-alpaca/paper-trading/)
  - [Yahoo Finance](https://www.yahoofinanceapi.com/)

<p align="center">
  <img src="https://simpleicons.org/icons/python.svg" alt="Python" width="50" height="50"/>
  <img src="https://simpleicons.org/icons/pandas.svg" alt="pandas" width="50" height="50"/>
  <img src="https://simpleicons.org/icons/transformers.svg" alt="transformers" width="50" height="50"/>
  <img src="https://simpleicons.org/icons/pytorch.svg" alt="torch" width="50" height="50"/>
  <img src="https://simpleicons.org/icons/alpaca.svg" alt="Alpaca" width="50" height="50"/>
  <img src="https://simpleicons.org/icons/yahoofinance.svg" alt="Yahoo Finance" width="50" height="50"/>
</p>

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
