import requests
import decimal
import requests_cache
from datetime import timedelta

expire_after = timedelta(minutes=15)
requests_cache.install_cache('demo_cache', expire_after=expire_after)


def get_usd():
    res = requests.get('https://blockchain.info/ticker')
    exchange_rate = res.json()['USD']['last']
    return decimal.Decimal(exchange_rate)
