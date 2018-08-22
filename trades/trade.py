class Trade(object):
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
