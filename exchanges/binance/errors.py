class BinanceAPIError(Exception):
    def __init__(self, message):
        self.message = message


class APIConnectivityError(BinanceAPIError):
    pass


class InvalidCredentialsError(BinanceAPIError):
    pass


class InvalidCurrencyError(BinanceAPIError):
    pass

