from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault

from wallets.models import Wallet


class WalletSerializer(ModelSerializer):
    # def create(self, validated_data):
    #     # user = self.context['request'].user
    #     wallet = Wallet.objects.create(
    #         owner=CurrentUserDefault(),
    #         **validated_data
    #     )
    #     return wallet

    class Meta:
        model = Wallet
        fields = ['address', 'bts']
