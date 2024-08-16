# Pionex to Python
> pip install pionex_python
# Description
Connector library for Pionex Restful and Websocket api.  
Closely resembles https://pionex-doc.gitbook.io/apidocs for intuitive implementation.  
All function names are identical to the names in documentation.
# Examples
## Restful  
```py
from pionex_python.restful.Common import Common

commonClient = Common()
market_data = commonClient.market_data()

print(market_data)
```

```py
from pionex_python.restful.Orders import Orders

key, secret = "XXXXX", "XXXXX"

ordersClient = Orders(key, secret)
response = ordersClient.new_order(
    symbol="BTC_USDT",
    side="BUY",
    type="MARKET",
    amount="16",
)
print(response)
```
## Websocket:
```py
from pionex_python.websocket.PublicStream import PublicStream
from time import sleep

stream = PublicStream()

def onMessage(msg):
    print(msg)

stream.subscribe(callback=onMessage, topic="TRADE",symbol="BTC_USDT")
sleep(5)
stream.unsubscribe(topic="TRADE",symbol="BTC_USDT")
```
# Motivation
- learn about the python packaging and publishing systems
- implement a websocket api client from 'scratch'
- increase experience with python and crypto marketplaces (other than binance)