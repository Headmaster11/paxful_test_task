import requests
import decimal


def get_usd():
    res = requests.get('https://blockchain.info/ticker')
    exchange_rate = res.json()['USD']['last']
    return decimal.Decimal(exchange_rate)
