from django.forms import ValidationError
from django.db.models import Q
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins, status

from wallets.models import Wallet
from wallets.serializers import WalletSerializer
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class WalletViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == 'transactions':
            return Wallet.objects.all()
        return Wallet.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        wallet = WalletSerializer(data=request.data)
        if wallet.is_valid():
            try:
                wallet.save(owner=request.user)
            except ValidationError:
                return Response({'error': 'max number of wallets'}, status.HTTP_400_BAD_REQUEST)
            return Response(wallet.data, status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def transactions(self, request, pk):
        data = Transaction.objects.filter(Q(from_wallet__pk=pk) | Q(to_wallet__pk=pk))
        return Response(TransactionSerializer(data, many=True).data)
