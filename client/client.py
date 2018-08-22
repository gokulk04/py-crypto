import exchanges.constants as ExchangeConstants
from exchanges.binance.binance import Binance


class Client(object):
    def __init__(self, exchange, api_key, api_secret):
        self.exchange = exchange
        self.api_key = api_key
        self.api_secret = api_secret

    def initialize(self):
        if self.exchange == ExchangeConstants.BINANCE:
            return Binance(api_key=self.api_key,
                           api_secret=self.api_secret).initialize()
