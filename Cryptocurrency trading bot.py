import cbpro
import pandas as pd
import numpy as np

class CryptoTradingBot:
    def __init__(self, api_key, api_secret, api_passphrase):
        self.client = cbpro.AuthenticatedClient(api_key, api_secret, api_passphrase)
        self.trading_pair = 'BTC-USD'
        self.interval = 300  # 5 minutes interval

    def get_historical_data(self):
        historical_data = self.client.get_product_historic_rates(self.trading_pair, granularity=self.interval)
        df = pd.DataFrame(historical_data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
        return df

    def calculate_indicators(self, df):
        df['SMA_50'] = df['close'].rolling(window=50).mean()
        df['SMA_200'] = df['close'].rolling(window=200).mean()
        df['RSI'] = self.calculate_rsi(df['close'], 14)
        return df

    def calculate_rsi(self, prices, window=14):
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def execute_trade(self):
        df = self.get_historical_data().iloc[::-1]
        df = self.calculate_indicators(df)
        latest_data = df.iloc[-1]
        
        if latest_data['SMA_50'] > latest_data['SMA_200'] and latest_data['RSI'] < 70:
            # Place buy order
            self.client.place_market_order(product_id=self.trading_pair, side='buy', funds=100)
            print("Buy order placed")
        elif latest_data['SMA_50'] < latest_data['SMA_200'] and latest_data['RSI'] > 30:
            # Place sell order
            self.client.place_market_order(product_id=self.trading_pair, side='sell', funds=100)
            print("Sell order placed")
        else:
            print("No action needed")

if __name__ == "__main__":
    # Replace these values with your Coinbase API credentials
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    api_passphrase = 'YOUR_API_PASSPHRASE'

    bot = CryptoTradingBot(api_key, api_secret, api_passphrase)
    bot.execute_trade()
#Note :
#Ensure that you have the required libraries installed. You can install them using pip:
#pip install cbpro pandas numpy
#Replace the placeholder values 'YOUR_API_KEY', 'YOUR_API_SECRET', and 'YOUR_API_PASSPHRASE' with your actual Coinbase API credentials.
