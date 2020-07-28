from rest_framework.serializers import ModelSerializer, SerializerMethodField

from wallets.models import Wallet


class WalletSerializer(ModelSerializer):
    address = SerializerMethodField(required=False)

    def get_address(self, obj):
        return obj.address

    class Meta:
        model = Wallet
        fields = ['address', 'bts']
