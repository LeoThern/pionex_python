class PionexException(Exception):
    pass

class WebsocketError(PionexException):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message

class REST_Exception(PionexException):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message

def get_rest_exception(exception_str):
    error_string_map = {
        'MARKET_INVALID_SYMBOL': 'Invalid symbol.',
        'MARKET_PARAMETER_ERROR': 'Parameter error',
        'TRADE_INVALID_SYMBOL': 'InvalidSymbol',
        'TRADE_PARAMETER_ERROR': 'ParameterError',
        'TRADE_OPERATION_DENIED': 'OperationDenied',
        'TRADE_ORDER_NOT_FOUND': 'OrderNotFound',
        'TRADE_NOT_ENOUGH_MONEY': 'NotEnoughMoney',
        'TRADE_PRICE_FILTER_DENIED': 'PriceFilterDenied',
        'TRADE_SIZE_FILTER_DENIED': 'SizeFilterDenied',
        'TRADE_AMOUNT_FILTER_DENIED': 'AmountFilterDenied',
        'TRADE_REPEAT_CLIENT_ORDER_ID': 'RepeatClientOrderId',
        'TRADE_OPEN_ORDER_EXCEED_LIMIT': 'OpenOrderExceedLimit',
    }
    
    if exception_str in exception_map:
        return REST_Exception(error_string_map[exception_str])
    else:
        raise ValueError(f"No exception defined for '{exception_str}'")