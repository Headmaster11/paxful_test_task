from rest_framework.serializers import ModelSerializer

from wallets.models import Wallet


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
