import trades.constants as Constants


class Trade(object):

    ORDER_TYPE_LIMIT = Constants.ORDER_TYPE_LIMIT
    ORDER_TYPE_MARKET = Constants.ORDER_TYPE_MARKET
    ORDER_ACTION_BUY = Constants.ORDER_ACTION_BUY
    ORDER_ACTION_SELL = Constants.ORDER_ACTION_SELL

    def __init__(self, ticker, action, quantity, order_type, price=None):
        self.ticker = ticker
        self.action = action
        self.quantity = quantity
        self.order_type = order_type
        self.price = price

    def get_ticker(self):
        return self.ticker

    def get_action(self):
        return self.action

    def get_quantity(self):
        return self.quantity

    def get_order_type(self):
        return self.order_type

    def get_price(self):
        return self.price
