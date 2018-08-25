class BinanceAPIError(Exception):
    def __init__(self, message):
        self.message = message
        print(message)


class APIConnectivityError(BinanceAPIError):
    pass


class InvalidAPICredentialsError(BinanceAPIError):
    pass


class InvalidCurrencyError(BinanceAPIError):
    pass

