import exchanges.constants as Constants


class Exchange(object):
    BINANCE = Constants.BINANCE
    BITTREX = Constants.BITTREX

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
