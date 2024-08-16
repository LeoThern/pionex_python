from pionex_python.internal.RestClient import RestClient
from pionex_python.internal.PionexExceptions import assert_valid_market_type

class Markets(RestClient):
    def __init__(self):
        super().__init__()

    def get_trades(self, symbol: str, limit: int = None):
        return self._send_request('GET', '/api/v1/market/trades', symbol=symbol, limit=limit)

    def get_depth(self, symbol: str, limit: int = None):
        return self._send_request('GET', '/api/v1/market/depth', symbol=symbol, limit=limit)

    def get_24hr_ticker(self, symbol: str = None, type: str = None):
        assert_valid_market_type(type)
        return self._send_request('GET', '/api/v1/market/tickers', symbol=symbol, type=type)

    def get_book_ticker(self, symbol: str = None, type: str = None):
        assert_valid_market_type(type)
        return self._send_request('GET', '/api/v1/market/bookTickers', symbol=symbol, type=type)

    def get_klines(self, symbol: str, interval: str, endTime: int = None, limit: int = None):
        return self._send_request('GET', '/api/v1/market/klines', symbol=symbol, interval=interval, endTime=endTime, limit=limit)
