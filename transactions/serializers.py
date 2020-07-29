from django.forms import ValidationError
from rest_framework.serializers import ModelSerializer

from transactions.models import Transaction


class TransactionSerializer(ModelSerializer):
    def validate_amount(self, value):
        if value <= 0:
            raise ValidationError('wrong amount')
        return value

    class Meta:
        model = Transaction
        fields = '__all__'
