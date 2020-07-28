from rest_framework.viewsets import ModelViewSet

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
