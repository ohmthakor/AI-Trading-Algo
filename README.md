still need to add images of charts and graphs, actal code, logs file

# AI Trading Bot

## Overview

MLTrader is an algorithmic trading strategy implemented using the Lumibot framework. The strategy combines technical indicators, such as RSI (Relative Strength Index), with AI-driven sentiment analysis to make informed trading decisions. It operates on a list of specified symbols from the S&P 500, executing trades based on market conditions and news sentiment.



## Technologies

  <p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas"/>
  <img src="https://img.shields.io/badge/Transformers-FF5733?style=for-the-badge&logo=transformers&logoColor=white" alt="Transformers"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/Alpaca-000000?style=for-the-badge&logo=alpaca&logoColor=white" alt="Alpaca"/>
  <img src="https://img.shields.io/badge/Yahoo_Finance-720E9E?style=for-the-badge&logo=yahoo&logoColor=white" alt="Yahoo Finance"/>
  <img src="https://img.shields.io/badge/FinBERT-0091EA?style=for-the-badge&logoColor=white" alt = FinBERT"/>
</p> 


## APIs

  #### Alpaca Trade REST API: 
  Utilized for executing trades, fetching news, and accessing market data. It is accessed through the alpaca_trade_api.REST client and the Alpaca class from lumibot.brokers. 

  #### Yahoo Finance Data:
  Used for backtesting your strategy using historical market data from Yahoo Finance.

 #### FinBERT on Hugging Face:
  Sentiment analysis model used to estimate sentiment from news headlines.

## Graphs
  <img width="1465" alt="Screenshot 2024-08-27 at 5 15 03 PM" src="https://github.com/user-attachments/assets/f0916e17-33e9-44c2-952e-be16ba5d24ad">
  <img width="630" alt="Screenshot 2024-08-27 at 5 15 33 PM" src="https://github.com/user-attachments/assets/d06652a4-c837-4c69-b60d-8bffd230663e">
  <img width="1198" alt="Screenshot 2024-08-27 at 5 16 27 PM" src="https://github.com/user-attachments/assets/24af25e1-48c5-43b0-9622-5558369632fc">
  <img width="630" alt="Screenshot 2024-08-27 at 5 15 33 PM" src="https://github.com/user-attachments/assets/6a027b2f-db60-421d-9c99-3b920dd1f075">


## Features

  ### Technical Analysis: 
  Utilizes the RSI (Relative Strength Index) and Bollinger Bands, and trailing stop-loss to identify potential buy and sell signals.
  ### Sentiment Analysis: 
  Implements AI-driven sentiment analysis using the FinBERT model to gauge market sentiment from news headlines.
  ### Automated Trading: 
  Executes trades based on combined signals from RSI and sentiment analysis.
  ### Backtesting: 
  Supports backtesting with historical data from Yahoo Finance to evaluate strategy performance before live trading.
  ### Risk Management: 
  Includes risk management features such as setting cash at risk and using bracket orders for take-profit and stop-loss.
