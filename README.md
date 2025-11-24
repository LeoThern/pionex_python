# Pionex to Python
```sh
pip install pionex_python
```
## Description
Connector library for Pionex Restful and Websocket api.
Closely resembles [PionexAPI Docs](https://pionex-doc.gitbook.io/apidocs) for intuitive implementation.
All function names are identical to the endpoints in the documentation.
## Examples
#### rest public
```py
from pionex_python.restful.Common import Common

commonClient = Common()
market_data = commonClient.market_data()

print(market_data)
```
#### rest private
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

stream.subscribe(onMessage=onMessage, topic='TRADE',symbol='BTC_USDT')
stream.subscribe(onMessage=onMessage, topic='TRADE',symbol='ETH_USDT')
sleep(5)
stream.unsubscribe(topic='TRADE',symbol='BTC_USDT')
stream.unsubscribe(topic='TRADE',symbol='ETH_USDT')
```

#### Demultiplexing Topic and Symbol
The websocket client demultiplexes multiple streams over a single connection. Each subscription to a unique (topic, symbol) pair can have its own callback function.

## Contributing
Contributions are welcome! Anyone can fork the repository, make changes, and submit a pull request for review and merging.

---

## Motivation
I initially developed this project to learn Python packaging, implement a WebSocket client, and gain experience with marketplace APIs.
