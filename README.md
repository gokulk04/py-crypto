# py-crypto
[![PyPI version](https://badge.fury.io/py/py-crypto.svg)](https://badge.fury.io/py/py-crypto)

## About
**py-crypto** is an open-source, cryptocurrency trading library for Python. This library is ideal for developers who wish to be able to interact with API endpoints of multiple cryptocurrency exchanges at once without wanting to write code specific to each. Simply specify which exchange you would like to interact with by name, along with your API credentials, as shown in the Example section below. Currently, the library offers API support for the following exchanges: [Binance](https://www.binance.com/) and [Bittrex](https://www.bittrex.com/).

## Installation
The source code is currently hosted on GitHub at https://github.com/gokulk04/py-crypto

The latest released version is also available for download via pip:
```python
pip install py-crypto
```

## Example

```python
import pycrypto.client as pyc

BINANCE_API_KEY = "MY_BINANCE_API_KEY"
BINANCE_API_SECRET = "MY_BINANCE_API_SECRET"

binance = pyc.Client(pyc.Exchange.BINANCE, BINANCE_API_KEY, BINANCE_API_SECRET)

binance.get_all_balances()
```
