import exchanges.constants as ExchangeConstants
from exchanges.bittrex.bittrex import Bittrex
from exchanges.binance.binance import Binance


class Exchange(object):
    BINANCE = ExchangeConstants.BINANCE
    BITTREX = ExchangeConstants.BITTREX

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

