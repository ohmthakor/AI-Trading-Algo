from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime
from alpaca_trade_api import REST
from timedelta import Timedelta
from ai_sent import estimate_sentiment
from ta.momentum import RSIIndicator

API_KEY = "Your API KEY"
API_SECRET = "your API Secret"
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    def initialize(self, symbols=None, cash_at_risk=0.5, max_trade_size=0.1, trailing_stop_percent = 0.05):
        if symbols is None:
            symbols = ["SPY"]
        self.symbols = symbols
        self.sleeptime = "24H"
        self.last_trades = {symbol: None for symbol in symbols}
        self.highest_prices = {symbol: None for symbol in symbols}
        self.trailing_stop_percent = trailing_stop_percent
        self.cash_at_risk = cash_at_risk
        self.max_trade_size = max_trade_size  # Cap on maximum trade size
        self.api = REST(base_url=BASE_URL, key_id=API_KEY, secret_key=API_SECRET)

    def position_sizing(self, symbol):
        cash = self.get_cash()
        last_price = self.get_last_price(symbol)
        if last_price is None:
            self.log_message(f"No price data for {symbol}", level="WARNING")
            return cash, None, 0
        
        # Calculate quantity with a cap on max trade size
        quantity = round(cash * min(self.cash_at_risk, self.max_trade_size) / last_price, 0)
        quantity = max(1, min(quantity, cash // last_price))
        return cash, last_price, quantity

    def get_dates(self):
        today = self.get_datetime()
        three_days_prior = today - Timedelta(days=3)
        return today.strftime('%Y-%m-%d'), three_days_prior.strftime('%Y-%m-%d')

    def get_sentiment(self, symbol):
        today, three_days_prior = self.get_dates()
        news = self.api.get_news(symbol=symbol, start=three_days_prior, end=today)
        news = [ev.__dict__["_raw"]["headline"] for ev in news]
        probability, sentiment = estimate_sentiment(news)
        return probability, sentiment

    def log_trade(self, symbol, action, quantity, last_price):
        message = f"{action.capitalize()} {quantity} shares of {symbol} at ${last_price:.2f}"
        self.log_message(message)
    
    def log_portfolio_state(self):
        cash = self.get_cash()
        portfolio_value = self.get_portfolio_value()
        self.log_message(f"Portfolio value: ${portfolio_value:.2f}, Cash: ${cash:.2f}")

    def calculate_rsi(self, symbol, window=14):
        data = self.get_historical_prices(symbol, length=365, timestep='day')
        df = data.df
        if df is None or len(df) < window:
            self.log_message(f"Not enough data to calculate RSI for {symbol}", level="WARNING")
            return None
        rsi = RSIIndicator(df['close'], window=window).rsi()
        return rsi.iloc[-1]

    def on_trading_iteration(self):
        rsi_buy_threshold = 50
        rsi_sell_threshold = 50

        for symbol in self.symbols:
            cash, last_price, quantity = self.position_sizing(symbol)
            if last_price is None:
                continue  # Skip if no price data

            rsi = self.calculate_rsi(symbol)
            if rsi is None:
                continue  # Skip if RSI couldn't be calculated

            if cash >= last_price * quantity:  # Ensure enough cash to buy
                if rsi <= rsi_buy_threshold:
                    if self.last_trades[symbol] == "sell":
                        self.sell_all()
                    order = self.create_order(
                        symbol,
                        quantity,
                        "buy",
                        type="market"
                    )
                    self.submit_order(order)
                    self.last_trades[symbol] = "buy"
                    self.highest_prices[symbol] = last_price  # Set initial highest price
                    self.log_trade(symbol, "buy", quantity, last_price)
                
            if self.last_trades[symbol] == "buy":
                # Update the highest price if the current price is higher
                if last_price > self.highest_prices[symbol]:
                    self.highest_prices[symbol] = last_price

                # Calculate the trailing stop price
                trailing_stop_price = self.highest_prices[symbol] * (1 - self.trailing_stop_percent)

                # Sell if the last price falls below the trailing stop price
                if last_price <= trailing_stop_price:
                    self.sell_all()
                    self.last_trades[symbol] = "sell"
                    self.log_trade(symbol, "sell", quantity, last_price)

            # Log portfolio state after each iteration
            self.log_portfolio_state()

# Define the list of S&P 500 symbols
sp500_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "LLY", "JPM", "WMT", "KO", "NFLX", "CRM", "ORCL"]  # Add more symbols as needed

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 8, 15)
broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker, parameters={"symbols": sp500_symbols, "cash_at_risk": 0.5, "max_trade_size": 0.1})

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={"symbols": sp500_symbols, "cash_at_risk": 0.5, "max_trade_size": 0.1}
)

# trader = Trader()
# trader.add_strategy(strategy)
# trader.run_all()