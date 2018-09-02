from exchanges.exchange import Exchange
from exchanges.binance.binance import Binance
from exchanges.bittrex.bittrex import Bittrex
from trades.trade import Trade


class Client(object):

    def __init__(self, exchange, api_key, api_secret):
        self.exchange = exchange
        self.api_key = api_key
        self.api_secret = api_secret
        self._initialize()

    def _initialize(self):
        return self._get_exchange().initialize()

    def get_current_price(self, ticker):
        return self._get_exchange().get_current_price(ticker)

    def get_ticker(self, ticker):
        return self._get_exchange().get_ticker(ticker)

    def get_open_orders(self, ticker=None):
        return self._get_exchange().get_open_orders(ticker)

    def get_order_history(self, ticker=None):
        return self._get_exchange().get_order_history(ticker)

    def get_all_balances(self):
        return self._get_exchange().get_all_balances()

    def get_balance(self, currency):
        return self._get_exchange().get_balance(currency)

    def create_market_order(self, ticker, action, quantity):
        trade = Trade(ticker, action, quantity, Trade.ORDER_TYPE_MARKET)
        return self._get_exchange().create_market_order(trade)

    def create_limit_order(self, ticker, action, quantity, price):
        trade = Trade(ticker, action, quantity, Trade.ORDER_TYPE_LIMIT, price)
        return self._get_exchange().create_limit_order(trade)

    def cancel_order(self, order_id, ticker=None):
        return self._get_exchange().cancel_order(order_id, ticker)

    def get_order_status(self, order_id, ticker=None):
        return self._get_exchange().get_order_status(order_id, ticker)

    def _get_exchange(self):
        if self.exchange == Exchange.BINANCE:
            return Binance(self.api_key, self.api_secret)
        if self.exchange == Exchange.BITTREX:
            return Bittrex(self.api_key, self.api_secret)
