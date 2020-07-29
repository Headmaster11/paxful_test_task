from rest_framework.serializers import ModelSerializer, SerializerMethodField

from wallets.models import Wallet
from utilities.get_rate import get_usd


class WalletSerializer(ModelSerializer):
    usd = SerializerMethodField()

    def get_usd(self, obj):
        return get_usd() * obj.bts

    class Meta:
        model = Wallet
        fields = ['address', 'bts', 'usd']
        extra_kwargs = {'address': {'required': False}}
