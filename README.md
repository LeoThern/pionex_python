# Pionex to Python
## Description
Connector library for Pionex Restful and Websocket api.
Closely resembles [PionexAPI Docs](https://pionex-doc.gitbook.io/apidocs) for intuitive implementation.
All function names are identical to the names in documentation.
## Examples
```sh
pip install pionex_python
```
### Restful
#### public
```py
from pionex_python.restful.Common import Common

commonClient = Common()
market_data = commonClient.market_data()

print(market_data)
```
#### private
```py
from pionex_python.restful.Orders import Orders

key, secret = 'X...X', 'X...X'

ordersClient = Orders(key, secret)

order = {
    'symbol':'BTC_USDT',
    'side':'BUY',
    'type':'MARKET',
    'amount':'16',
}

response = ordersClient.new_order(order=order)
print(response)
```

<details>
  <summary>Multiple Order Template</summary>

  ```py
  from pionex_python.restful.Orders import Orders

  key, secret = 'X...X', 'X...X'

  ordersClient = Orders(key, secret)

  orders = [
    {
    'side':'BUY',
    'type':'LIMIT',
    'price':'57200',
    'size':'0.0002'
    },{
    'side':'SELL',
    'type':'LIMIT',
    'price':'60000',
    'size':'0.0002'
    }
  ]

  response = ordersClient.new_multiple_order(symbol='BTC_USDT',orders=orders)
  print(response)
  ```
</details>

### Websocket
```py
from pionex_python.websocket.PublicStream import PublicStream
from time import sleep

#stream = PrivateStream(key, secret)
stream = PublicStream()

def onMessage(msg):
    print(msg)

stream.subscribe(callback=onMessage, topic='TRADE',symbol='BTC_USDT')
sleep(5)
stream.unsubscribe(topic='TRADE',symbol='BTC_USDT')
```
## Motivation
- learn about the python packaging and publishing systems
- implement a python websocket client
- increase experience with marketplace apis
