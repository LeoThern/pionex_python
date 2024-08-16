from pionex_python.internal.RestClient import RestClient

class Orders(RestClient):
    def __init__(self, key, secret):
        super().__init__(key, secret)

    @staticmethod
    def assert_valid_order_side_type(side, type):
        assert side in ['BUY', 'SELL'], "unknown side"
        assert type in ['LIMIT', 'MARKET'], "unknown type"

    @staticmethod
    def assert_valid_mass_orders(orders):
        for order in orders:
            assert order['side'] in ['BUY', 'SELL'], "unknown side"
            assert order['type'] == 'LIMIT', "mass orders only support LIMIT"
            assert order['size'], "order needs to have a size"
            assert order['price'], "limit oder needs to have a price"

    def new_order(self, symbol: str, side: str, type: str, clientOrderId: str = None, size: str = None, price: str = None, amount: str = None, IOC: bool = None):
        self.assert_valid_order_side_type(side, type)
        data = {
          "symbol": symbol,
          "side": side,
          "type": type,
          "clientOrderId": clientOrderId,
          "size": size,
          "price": price,
          "amount": amount,
          "IOC": IOC,
        }
        return self._send_request('POST', '/api/v1/trade/order', data=data)

    def new_multiple_order(self, symbol: str, orders: list = None):
        self.assert_valid_mass_orders(orders)
        data = {
            "symbol": symbol,
            "orders": orders
        }
        return self._send_request('POST', '/api/v1/trade/massOrder', data=data)

    def get_order(self, orderId: int):
        return self._send_request('GET', '/api/v1/trade/order', orderId=orderId)

    def get_order_by_client_order_id(self, clientOrderId: int):
        return self._send_request('GET', '/api/v1/trade/orderByClientOrderId', clientOrderId=clientOrderId)

    def cancel_order(self, symbol: str, orderId: int):
        data = {'symbol':symbol, 'orderId':orderId}
        return self._send_request('DELETE', '/api/v1/trade/order', data=data)

    def get_open_orders(self, symbol: str):
        return self._send_request('GET', '/api/v1/trade/openOrders', symbol=symbol)

    def get_all_orders(self, symbol: str, startTime: int = None, endTime: int = None, limit: int = None):
        return self._send_request('GET', '/api/v1/trade/allOrders', symbol=symbol, startTime=startTime, endTime=endTime, limit=limit)

    def get_fills(self, symbol: str, startTime: int = None, endTime: int = None):
        return self._send_request('GET', '/api/v1/trade/fills', symbol=symbol, startTime=startTime, endTime=endTime)

    def get_fills_by_order_id(self, orderId: int, fromId: int = None):
        return self._send_request('GET', '/api/v1/trade/fillsByOrderId', orderId=orderId, fromId=fromId)

    def cancel_all_orders(self, symbol: str):
        data = {'symbol':symbol}
        return self._send_request('DELETE', '/api/v1/trade/allOrders', data=data)
