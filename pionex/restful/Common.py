from pionex.restful.RestClient import RestClient

class Common(RestClient):
    def __init__(self):
        super().__init__()

    def market_data(self, symbols:list[str], type:str=None):
        if type:
            assert type in ['SPOT', 'PERP'], "unsupported type"
        return self._send_request('GET', '/api/v1/common/symbols', symbols=symbols, type=type)
