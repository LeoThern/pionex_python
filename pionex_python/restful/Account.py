from pionex_python.internal.RestClient import RestClient

class Account(RestClient):
    def __init__(self, key, secret):
        super().__init__(key, secret)

    def get_balance(self):
        return self._send_request('GET', '/api/v1/account/balances')