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
        pass

    def create_limit_order(self, trade_obj):
        # endpoint = Bittrex._get_trade_signal(trade_obj.get_action())
        # new_params = {
        #     "market": trade_obj.get_ticker(),
        #     "quantity": trade_obj.get_quantity(),
        #     "rate": trade_obj.get_price()
        # }
        pass

    @staticmethod
    def _get_trade_signal(signal):
        # if signal == "SELL":
        #     return EndpointConstants.ORDER_BUY_LIMIT
        # elif signal == "BUY":
        #     return EndpointConstants.ORDER_BUY_LIMIT
        # else:
        #     return None
        pass

    def create_market_order(self, trade_obj):
        pass

    def _create_order(self, params):
        pass

    def cancel_order(self, order_id, symbol=None):
        pass

    def get_order_status(self, order_id, symbol=None):
        endpoint = EndpointConstants.GET_ORDER
        new_params = {
            "uuid": order_id
        }

        return self._make_request(endpoint, new_params)

    def get_order_history(self, symbol=None):
        endpoint = EndpointConstants.GET_ORDER_HISTORY
        new_params = {}
        if symbol is not None:
            new_params["market"] = symbol

        return self._make_request(endpoint, new_params)

    def get_balance(self, asset):
        endpoint = EndpointConstants.GET_BALANCE
        new_params = {
            "currency": asset
        }

        return self._make_request(endpoint, new_params)

    def get_all_balances(self):
        endpoint = EndpointConstants.GET_ALL_BALANCES

        return self._make_request(endpoint)

    def _make_request(self, endpoint, new_params=None):
        params = self._create_params(new_params)
        url = self._get_request_string(endpoint, params)
        signature = Utils.hash_hmac_sha512(self.api_secret, url)

        return Utils.to_json(
            requests.get(url=url,
                         params="",
                         headers=self._get_request_header(signature))
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