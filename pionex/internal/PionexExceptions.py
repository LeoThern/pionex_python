class PionexException(Exception):
    pass

class WebsocketError(PionexException):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message

class REST_Exception(PionexException):
    def __init__(self, response):
        self.code = response['code']
        self.message = response['message']

    def __str__(self):
        return f"{self.code} \n[!] {self.message}"


def assert_valid_market_type(type_str):
    if type_str:
        assert type in ['SPOT','PERP'], "unknown type"
