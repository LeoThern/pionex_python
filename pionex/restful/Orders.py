from pionex.internal.RestClient import RestClient

class Orders(RestClient):
    def __init__(self, key, secret):
        super().__init__(key, secret)

    def new_order(self, symbol: str, side: str, type: str, clientOrderId: str = None, size: str = None, price: str = None, amount: str = None, IOC: bool = None):
        return self._send_request('POST', '/api/v1/trade/order',
                                symbol=symbol, side=side, type=type,
                                clientOrderId=clientOrderId, size=size,
                                price=price, amount=amount, IOC=IOC)

    def new_multiple_order(self, symbol: str, side: str, type: str, size: str, price: str, clientOrderId: str = None, orders: list = None):
        return self._send_request('POST', '/api/v1/trade/massOrder',
                                symbol=symbol,
                                side=side,
                                type=type,
                                size=size,
                                price=price,
                                clientOrderId=clientOrderId,
                                orders=orders)

    def get_order(self, orderId: int):
        return self._send_request('GET', '/api/v1/trade/order', orderId=orderId)

    def get_order_by_client_order_id(self, clientOrderId: int):
        return self._send_request('GET', '/api/v1/trade/orderByClientOrderId', clientOrderId=clientOrderId)

    def cancel_order(self, symbol: str, orderId: int):
        return self._send_request('DELETE', '/api/v1/trade/order', symbol=symbol, orderId=orderId)

    def get_open_orders(self, symbol: str):
        return self._send_request('GET', '/api/v1/trade/openOrders', symbol=symbol)

    def get_all_orders(self, symbol: str, startTime: int = None, endTime: int = None, limit: int = None):
        return self._send_request('GET', '/api/v1/trade/allOrders', symbol=symbol, startTime=startTime, endTime=endTime, limit=limit)

    def get_fills(self, symbol: str, startTime: int = None, endTime: int = None):
        return self._send_request('GET', '/api/v1/trade/fills', symbol=symbol, startTime=startTime, endTime=endTime)

    def get_fills_by_order_id(self, orderId: int, fromId: int = None):
        return self._send_request('GET', '/api/v1/trade/fillsByOrderId', orderId=orderId, fromId=fromId)

    def cancel_all_orders(self, symbol: str):
        return self._send_request('DELETE', '/api/v1/trade/allOrders', symbol=symbol)
