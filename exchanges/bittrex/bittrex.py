import time
import urllib
import requests
from utils.utils import Utils
import exchanges.bittrex.constants.endpoints as EndpointConstants


class Bittrex(object):
    HEADERS = {}

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def initialize(self):
        if Bittrex.ping() is False:
            return False
        if self.get_all_balances()['success'] is False:
            return False
        return True

    @staticmethod
    def get_ticker_price(symbol):
        return float(Bittrex.get_ticker(symbol)['result']['Last'])

    @staticmethod
    def get_ticker(symbol):
        endpoint = EndpointConstants.GET_TICKER
        new_params = {
            "market": symbol
        }
        return Bittrex._make_public_request(endpoint, new_params)

    def create_limit_order(self, trade_obj):
        endpoint = Bittrex._get_trade_signal(trade_obj.get_action())
        new_params = {
            "market": trade_obj.get_ticker(),
            "quantity": trade_obj.get_quantity(),
            "rate": trade_obj.get_price()
        }

        return self._make_private_request(endpoint, new_params)

    @staticmethod
    def _get_trade_signal(signal):
        if signal == "SELL":
            return EndpointConstants.ORDER_BUY_LIMIT
        elif signal == "BUY":
            return EndpointConstants.ORDER_BUY_LIMIT
        else:
            return None

    def cancel_order(self, order_id, symbol=None):
        endpoint = EndpointConstants.ORDER_CANCEL
        new_params = {
            "uuid": order_id
        }

        return self._make_private_request(endpoint, new_params)

    def get_open_orders(self, symbol=None):
        endpoint = EndpointConstants.GET_OPEN_ORDERS
        new_params = {}
        if symbol is not None:
            new_params["market"] = symbol

        return self._make_private_request(endpoint, new_params)

    def get_order_status(self, order_id, symbol=None):
        endpoint = EndpointConstants.GET_ORDER
        new_params = {
            "uuid": order_id
        }

        return self._make_private_request(endpoint, new_params)

    def get_order_history(self, symbol=None):
        endpoint = EndpointConstants.GET_ORDER_HISTORY
        new_params = {}
        if symbol is not None:
            new_params["market"] = symbol

        return self._make_private_request(endpoint, new_params)

    def get_balance(self, asset):
        endpoint = EndpointConstants.GET_BALANCE
        new_params = {
            "currency": asset
        }

        return self._make_private_request(endpoint, new_params)

    def get_all_balances(self):
        endpoint = EndpointConstants.GET_ALL_BALANCES

        return self._make_private_request(endpoint)

    def _make_private_request(self, endpoint, new_params=None):
        params = self._create_params(new_params)
        url = self._get_request_string(endpoint, params)
        signature = Utils.hash_hmac_sha512(self.api_secret, url)

        return Utils.to_json(
            requests.get(url=url,
                         params="",
                         headers=self._get_request_header(signature))
        )

    @staticmethod
    def _make_public_request(endpoint, new_params=None):
        return Utils.to_json(
            requests.get(url=endpoint,
                         params=new_params,
                         headers="")
        )

    def _create_params(self, new_params=None):
        params = {
            "apikey": self.api_key,
            "nonce": str(time.time())
        }

        if new_params is not None:
            params.update(new_params)

        return urllib.urlencode(params)

    @staticmethod
    def _get_request_string(endpoint, params):
        return endpoint + "?" + params

    @staticmethod
    def _get_request_header(signature):
        return {
            "apisign": signature
        }

    @staticmethod
    def get_markets():
        endpoint = EndpointConstants.GET_MARKETS
        return Bittrex._make_public_request(endpoint)

    @staticmethod
    def ping():
        if Bittrex.get_markets()['success'] is True:
            return True
        return False
