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
        pass

    def get_all_balances(self):
        pass

    def get_account(self):
        pass

    def _create_signature(self, params):
        pass