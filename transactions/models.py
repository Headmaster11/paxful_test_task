from django.db import models
from django.contrib.auth.models import User

from wallets.models import Wallet


class Transaction(models.Model):
    from_wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True)
    to_wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True)
    platform_profit = models.FloatField()
