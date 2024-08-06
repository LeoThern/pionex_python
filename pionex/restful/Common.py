from pionex.internal.RestClient import RestClient

#rename python function so we can have "type" argument
type_func = type

class Common(RestClient):
    def __init__(self):
        super().__init__()

    def market_data(self, symbols:list[str], type:str=None):
        if type:
            assert type in ['SPOT', 'PERP'], "unsupported type"
        if type_func(symbols) == list:
            symbols = ','.join(symbols)
        return self._send_request('GET', '/api/v1/common/symbols', symbols=symbols, type=type)
