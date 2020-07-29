from django.forms import ValidationError
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins, status

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(from_wallet__owner=self.request.user)

    def create(self, request, *args, **kwargs):
        data = request.data
        transaction = TransactionSerializer(data=data)
        if transaction.is_valid():
            try:
                transaction.save()
            except ValidationError:
                return Response({'error': 'not enough bts'}, status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
