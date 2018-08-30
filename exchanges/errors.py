from errors.errors import Error
import exchanges.constants as ExchangeConstants


class ExchangeAPIError(Error):

    MESSAGE = None

    def __init__(self, exchange, message):
        Error.__init__(self, message)
        self.exchange = exchange

    def get_message(self):
        return self.exchange + " API Error: " + self.message

    def display(self):
        print self.get_message()

    def get_default_message(self):
        return self.MESSAGE


class InvalidAPICredentialsError(ExchangeAPIError):

    MESSAGE = ExchangeConstants.INVALID_API_CREDENTIALS_ERROR

    def __init__(self, exchange, message=None):
        if message:
            ExchangeAPIError.__init__(self, exchange, message)
        else:
            ExchangeAPIError.__init__(self, exchange, self.get_default_message())
