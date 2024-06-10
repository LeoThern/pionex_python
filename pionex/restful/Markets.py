from pionex.restful.RestClient import RestClient

class Markets(RestClient):
    def __init__():
        super().__init__()

    def get_trades(symbol:str, limit:int=None):
        return self._send_request('GET', '/api/v1/market/trades', symbol=symbol, limit=limit)

    def get_depth(symbol:str, limit:int=None):
        return self._send_request('GET', '/api/v1/market/depth', symbol=symbol, limit=limit)

    def get_24hr_ticker(symbol:str=None, type:str=None):
        return self._send_request('GET', '/api/v1/market/tickers', symbol=symbol, type=type)

    def get_book_ticker(symbol:str=None, type:str=None):
        return self._send_request('GET', '/api/v1/market/bookTickers', symbol=symbol, type=type)

    def get_klines(symbol:str, interval:str, endTime:int=None, limit:int=None):
        return self._send_request('GET', '/api/v1/market/klines', symbol=symbol, interval=interval, endTime=endTime, limit=limit)
