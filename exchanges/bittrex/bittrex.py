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
        pass

    def create_market_order(self, trade_obj):
        pass

    def _create_order(self, params):
        pass

    def cancel_order(self, symbol, order_id):
        pass

    def get_order_status(self, symbol, order_id):
        pass

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