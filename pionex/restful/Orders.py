from pionex.restful.RestClient import RestClient

class Common(RestClient):
    def __init__(key, secret):
        super().__init__(key, secret)

    def new_order():
        pass