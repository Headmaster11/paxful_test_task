from rest_framework.serializers import ModelSerializer

from transactions.models import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs = {'platform_profit': {'required': False}}
