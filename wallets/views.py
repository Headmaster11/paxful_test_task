from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins

from wallets.models import Wallet
from wallets.serializers import WalletSerializer


class WalletViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        WalletSerializer.save(request)
        return Response()
