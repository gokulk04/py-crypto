from global_errors.errors import Error
import exchanges.constants as ExchangeConstants


class ExchangeAPIError(Error):

    MESSAGE = None
    BINANCE = ExchangeConstants.Binance
    BITTREX = ExchangeConstants.Bittrex

    def __init__(self, exchange, message=None):
        if message:
            Error.__init__(self, message)
        else:
            Error.__init__(self, self.get_default_message())
        self.exchange = exchange
        self.display()

    def get_message(self):
        return self.exchange + " API Error: " + self.message

    def get_default_message(self):
        return self.MESSAGE


class InvalidAPICredentialsError(ExchangeAPIError):
    MESSAGE = ExchangeConstants.INVALID_API_CREDENTIALS_ERROR


class APIConnectionError(ExchangeAPIError):
    MESSAGE = ExchangeConstants.API_CONNECTION_ERROR


class InvalidCurrencyError(ExchangeAPIError):
    MESSAGE = ExchangeConstants.INVALID_CURRENCY_ERROR


class MarketOrderTypeUnavailableError(ExchangeAPIError):
    MESSAGE = ExchangeConstants.MARKET_ORDER_TYPE_UNAVAILABLE


class MissingParameterError(ExchangeAPIError):
    MESSAGE = ExchangeConstants.MISSING_PARAMETER_ERROR

    def __init__(self, exchange, param):
        MissingParameterError.MESSAGE = MissingParameterError.MESSAGE + param
        ExchangeAPIError.__init__(self, exchange)
