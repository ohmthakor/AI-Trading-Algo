# AI Trading Bot

## Overview

MLTrader is an algorithmic trading strategy implemented using the Lumibot framework. The strategy combines technical indicators, such as RSI (Relative Strength Index), with AI-driven sentiment analysis to make informed trading decisions. It operates on a list of specified symbols from the S&P 500, executing trades based on market conditions and news sentiment.



## Technologies

**Programming Languages**:
    ![Python]("https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white")
    
**Libraries**:
  - Lumibot
  - Alpaca <img src="https://simpleicons.org/icons/alpaca.svg" alt="Alpaca" width="30" height="30"/>
  - pandas <img src="https://simpleicons.org/icons/pandas.svg" alt="pandas" width="30" height="30"/>
  - transformers <img src="https://simpleicons.org/icons/transformers.svg" alt="transformers" width="30" height="30"/>
  - torch <img src="https://simpleicons.org/icons/pytorch.svg" alt="torch" width="30" height="30"/>
  - [ta](https://github.com/bukosabino/ta)
**Tools**:
  - Alpaca Paper Trading
  - Yahoo Finance <img src="https://simpleicons.org/icons/yahoofinance.svg" alt="Yahoo Finance" width="50" height="50"/>

  <p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas"/>
  <img src="https://img.shields.io/badge/Transformers-FF5733?style=for-the-badge&logo=transformers&logoColor=white" alt="Transformers"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/Alpaca-000000?style=for-the-badge&logo=alpaca&logoColor=white" alt="Alpaca"/>
  <img src="https://img.shields.io/badge/Yahoo_Finance-720E9E?style=for-the-badge&logo=yahoo&logoColor=white" alt="Yahoo Finance"/>
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
