from pionex.restful.RestClient import RestClient

class Account(RestClient):
    def __init__(key, secret):
        super().__init__(key, secret)

    def get_balance():
        return self._send_request('GET', '/api/v1/account/balances')