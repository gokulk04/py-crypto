import requests
from utils.utils import Utils
from trades.trade import Trade
from exchanges.exchange import Exchange
import exchanges.errors as Errors
import exchanges.binance.constants as Constants


class Binance(Exchange):

    HEADERS = {}

    def __init__(self, api_key, api_secret):
        Exchange.__init__(self, api_key, api_secret)
        # self.api_key = api_key
        # self.api_secret = api_secret
        self.initialize_headers()

    def initialize_headers(self):
        Binance.HEADERS["X-MBX-APIKEY"] = self.api_key

    def initialize(self):
        if bool(Binance.ping()) is not False:
            raise Errors.APIConnectionError(Errors.ExchangeAPIError.BINANCE)
        else:
            if 'balances' in self.get_account():
                return True
            raise Errors.InvalidAPICredentialsError(Errors.ExchangeAPIError.BINANCE)

    @staticmethod
    def get_server_time():
        return Utils.to_json(requests.get(Constants.TIME))['serverTime']

    @staticmethod
    def get_current_price(symbol):
        return float(Binance.get_ticker(symbol)['price'])

    @staticmethod
    def get_ticker(symbol):
        params = {
            "symbol": symbol
        }

        return Utils.to_json(
            requests.get(url=Constants.TICKER,
                         params=params
                         )
        )

    def get_order_history(self, symbol):

        if symbol is None:
            raise Errors.MissingParameterError(Errors.ExchangeAPIError.BINANCE, "symbol")

        params = {
            "symbol": symbol,
            "timestamp": Binance.get_server_time()
        }

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.get(url=Constants.All_ORDERS,
                         params=Binance.params_with_signature(params, signature),
                         headers=Binance.HEADERS
                         )
        )

    def get_open_orders(self, symbol=None):
        params = {
            "timestamp": Binance.get_server_time()
        }

        if symbol:
            params["symbol"] = symbol

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.get(url=Constants.OPEN_ORDERS,
                         params=Binance.params_with_signature(params, signature),
                         headers=Binance.HEADERS
                         )
        )

    def create_limit_order(self, trade_obj):
        params = Binance._create_trade_req_params(trade_obj)
        return self._create_order(params)

    def create_market_order(self, trade_obj):
        params = Binance._create_trade_req_params(trade_obj)
        return self._create_order(params)

    def _create_order(self, params):

        params["timestamp"] = Binance.get_server_time()

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.post(url=Constants.ORDER,
                          params=Binance.params_with_signature(params, signature),
                          headers=Binance.HEADERS)
        )

    def cancel_order(self, order_id, symbol):
        if symbol is None:
            raise Errors.MissingParameterError(Errors.ExchangeAPIError.BINANCE, "ticker")

        params = Binance._create_order_req_params(symbol, order_id)

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.delete(url=Constants.ORDER,
                            params=Binance.params_with_signature(params, signature),
                            headers=Binance.HEADERS)
        )

    def get_order_status(self, symbol, order_id):
        params = Binance._create_order_req_params(symbol, order_id)

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.get(url=Constants.ORDER,
                         params=Binance.params_with_signature(params, signature),
                         headers=Binance.HEADERS)
        )

    def get_balance(self, asset):
        balances = self.get_all_balances()
        for item in balances:
            if item['asset'] == asset:
                return float(item['free'])
        raise Errors.InvalidCurrencyError(Errors.ExchangeAPIError.BINANCE)

    def get_all_balances(self):
        data = self.get_account()
        return data['balances']

    def get_account(self):
        params = {
            "timestamp": Binance.get_server_time()
        }

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.get(url=Constants.ACCOUNT,
                         params=Binance.params_with_signature(params, signature),
                         headers=Binance.HEADERS)
        )

    def _create_signature(self, params):
        return Utils.hash_hmac_sha256(secret=self.api_secret,
                                      params=params)

    @staticmethod
    def params_with_signature(params, signature):
        params['signature'] = signature
        return params

    @staticmethod
    def ping():
        return Utils.to_json(requests.get(Constants.PING))

    @staticmethod
    def _create_order_req_params(symbol, order_id):
        return {
            "symbol": symbol,
            "order_id": order_id
        }

    @staticmethod
    def _create_trade_req_params(trade_obj):
        params = {
            "symbol": trade_obj.get_ticker(),
            "side": trade_obj.get_action(),
            "type": trade_obj.get_order_type(),
            "quantity": trade_obj.get_quantity(),
        }

        if trade_obj.get_order_type() == "LIMIT":
            params["timeInForce"] = "GTC"
            params["price"] = trade_obj.get_price()

        return params
