class Error(Exception):
    def __init__(self, message):
        self.message = message

    def display(self):
        print self.get_message()

    def get_message(self):
        return self.message


