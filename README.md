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

## APIs used:

  #### Alpaca Trade REST API: 
  This is used for executing trades, fetching news, and accessing market data. It is accessed through the alpaca_trade_api.REST client and the Alpaca class from lumibot.brokers. 

  #### Yahoo Finance Data:
  YahooDataBacktesting: This is used for backtesting your strategy using historical market data from Yahoo Finance.

 #### Hugging Face Transformers API:
  This library provides access to a wide variety of pre-trained models and tokenizers for natural language processing (NLP) tasks.
  AutoTokenizer: This class is used to download and load the tokenizer for the specified pre-trained model. The tokenizer converts text into token IDs that can be processed by the       model.
