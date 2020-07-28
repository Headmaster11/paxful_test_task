from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins, status

from wallets.models import Wallet
from wallets.serializers import WalletSerializer


class WalletViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        wallet = WalletSerializer(data=request.data)
        if wallet.is_valid():
            wallet.save(owner=request.user)
            return Response({'address': wallet.address})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
