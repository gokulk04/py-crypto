import requests
from utils.utils import Utils
import exchanges.binance.constants.endpoints as EndpointConstants
import exchanges.binance.constants.errors as ErrorConstants
import exchanges.binance.errors as BinanceErrors


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
            raise BinanceErrors.InvalidCredentialsError(ErrorConstants.INVALID_CREDENTIALS_ERROR_MESSAGE)

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

        signature = Utils.hash_request(secret=self.api_secret,
                                       params=params)

        return Utils.to_json(
            requests.get(url=EndpointConstants.ACCOUNT,
                         params=Binance.params_with_signature(params, signature),
                         headers=Binance.HEADERS)
        )

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

