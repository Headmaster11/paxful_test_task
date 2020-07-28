from django.conf import settings
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins, status

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from wallets.models import Wallet


class TransactionViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        transaction = TransactionSerializer(data=data)
        if transaction.is_valid():
            from_wallet = Wallet.objects.get(data['from_wallet'])
            to_wallet = Wallet.objects.get(data['to_wallet'])
            if from_wallet.owner != to_wallet.owner:
                transaction.save(platform_profit=data['amount'] * settings.PLATFORM_TRANSFER_CHARGE)
            else:
                transaction.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
