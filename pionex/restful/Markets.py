import RestClient

class Markets(RestClient):
    def __init__():
        super().__init__()

    #TODO add params to request

    def get_trades(symbol:str, limit:int=None):
        return self._send_request('GET', '/api/v1/market/trades', params)

    def get_depth(symbol:str, limit:int=None):
        return self._send_request('GET', '/api/v1/market/depth', params)

    def get_24hr_ticker(symbol:str=None, type:str=None):
        return self._send_request('GET', '/api/v1/market/tickers', params)

    def get_24hr_ticker(symbol:str=None, type:str=None):
        return self._send_request('GET', '/api/v1/market/bookTickers', params)

    def get_klines(symbol:str, interval:str, endTime:int=None, limit:int=None):
        return self._send_request('GET', '/api/v1/market/klines', params)
    