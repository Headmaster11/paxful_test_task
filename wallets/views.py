from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from wallets.models import Wallet
from wallets.serializers import WalletSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    authentication_classes = [TokenAuthentication]
