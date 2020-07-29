from rest_framework.serializers import ModelSerializer, SerializerMethodField

from wallets.models import Wallet

import requests


class WalletSerializer(ModelSerializer):
    usd = SerializerMethodField()

    def get_usd(self, obj):
        res = requests.get('https://blockchain.info/ticker')
        exchange_rate = res.json()['USD']['last']
        return exchange_rate * obj.bts

    class Meta:
        model = Wallet
        fields = ['address', 'bts', 'usd']
        extra_kwargs = {'address': {'required': False}}
