import requests
import json
import urllib
import hashlib
import hmac
from utils.utils import Utils
import exchanges.binance.constants.endpoints as EndpointConstants
import exchanges.binance.constants.errors as ErrorConstants
import exchanges.binance.errors as BinanceErrors

class Binance(object):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def initialize(self):
        if bool(Binance.ping()) is not False:
            raise BinanceErrors.APIConnectivityError(ErrorConstants.CONNECTIVITY_ERROR_MESSAGE)
        else:
            pass

    @staticmethod
    def get_server_time():
        return Utils.to_json(requests.get(EndpointConstants.TIME))['serverTime']

    def create_limit_order(self):
        pass

    def create_market_order(self):
        pass

    def create_order(self):
        pass

    def cancel_order(self):
        pass

    def get_order_status(self):
        pass

    def get_account_balance(self):
        pass

    def get_account(self):
        pass

    @staticmethod
    def ping():
        return Utils.to_json(requests.get(EndpointConstants.PING))

    @staticmethod
    def create_req_params(self):
        pass

