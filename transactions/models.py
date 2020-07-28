from django.db import models
from django.contrib.auth.models import User

from wallets.models import Wallet


class Transaction(models.Model):
    from_wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, related_name='transfer_from')
    to_wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, related_name='transfer_to')
    platform_profit = models.FloatField()
