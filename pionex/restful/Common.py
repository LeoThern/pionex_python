import RestClient

class Common(RestClient):
    def __init__():
        super().__init__()

    def market_data(symbols:list[str], type:str=None):
        if type:
            assert type in ['SPOT', 'PERP'], "unsupported type"
        return self._send_request('GET', '/api/v1/common/symbols', params)
