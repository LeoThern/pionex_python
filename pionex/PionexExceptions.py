class PionexException(Exception):
    pass

class WebsocketClientError(PionexException):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message