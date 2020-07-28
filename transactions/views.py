from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins, status

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        return Response(status=status.HTTP_201_CREATED)
