import requests
from utils.utils import Utils
from trades.trade import Trade
import exchanges.binance.errors as BinanceErrors
import exchanges.binance.constants.errors as ErrorConstants
import exchanges.binance.constants.endpoints as EndpointConstants


class Binance(object):

    HEADERS = {}

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.initialize_headers()

    def initialize_headers(self):
        Binance.HEADERS["X-MBX-APIKEY"] = self.api_key

    def initialize(self):
        if bool(Binance.ping()) is not False:
            raise BinanceErrors.APIConnectivityError(ErrorConstants.CONNECTIVITY_ERROR_MESSAGE)
        else:
            if 'balances' in self.get_account():
                return True
            raise BinanceErrors.InvalidAPICredentialsError(ErrorConstants.INVALID_CREDENTIALS_ERROR_MESSAGE)

    @staticmethod
    def get_server_time():
        return Utils.to_json(requests.get(EndpointConstants.TIME))['serverTime']

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

    @staticmethod
    def _create_order_req_params(symbol, order_id):
        return {
            "symbol": symbol,
            "order_id": order_id
        }

    def create_limit_order(self, trade_obj):
        params = Binance._create_trade_req_params(trade_obj)
        return self._create_order(params)

    # def create_limit_order(self, symbol, side, quantity, price):
    #     trade = Trade(symbol, side, quantity, "LIMIT", price)
    #     params = Binance._create_trade_req_params(trade)
    #
    #     return self._create_order(params)

    def create_market_order(self, trade_obj):
        params = Binance._create_trade_req_params(trade_obj)
        return self._create_order(params)

    # def create_market_order(self, symbol, side, quantity):
    #     trade = Trade(symbol, side, quantity, "MARKET")
    #     params = Binance._create_trade_req_params(trade)
    #
    #     return self._create_order(params)

    def _create_order(self, params):

        params["timestamp"] = Binance.get_server_time()

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.post(url=EndpointConstants.ORDER,
                          params=Binance.params_with_signature(params, signature),
                          headers=Binance.HEADERS)
        )

    def cancel_order(self, symbol, order_id):
        params = Binance._create_order_req_params(symbol, order_id)

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.delete(url=EndpointConstants.ORDER,
                            params=Binance.params_with_signature(params, signature),
                            headers=Binance.HEADERS)
        )

    def get_order_status(self, symbol, order_id):
        params = Binance._create_order_req_params(symbol, order_id)

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.get(url=EndpointConstants.ORDER,
                         params=Binance.params_with_signature(params, signature),
                         headers=Binance.HEADERS)
        )

    def get_balance(self, asset):
        balances = self.get_all_balances()
        for item in balances:
            if item['asset'] == asset:
                return float(item['free'])
        raise BinanceErrors.InvalidCurrencyError(ErrorConstants.INVALID_CURRENCY_ERROR_MESSAGE)

    def get_all_balances(self):
        data = self.get_account()
        return data['balances']

    def get_account(self):
        params = {
            "timestamp": Binance.get_server_time()
        }

        signature = self._create_signature(params)

        return Utils.to_json(
            requests.get(url=EndpointConstants.ACCOUNT,
                         params=Binance.params_with_signature(params, signature),
                         headers=Binance.HEADERS)
        )

    def _create_signature(self, params):
        return Utils.hash_request(secret=self.api_secret,
                                  params=params)

    @staticmethod
    def params_with_signature(params, signature):
        params['signature'] = signature
        return params

    @staticmethod
    def ping():
        return Utils.to_json(requests.get(EndpointConstants.PING))

    @staticmethod
    def create_req_params(self):
        pass

