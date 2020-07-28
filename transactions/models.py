from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User

from wallets.models import Wallet


class Transaction(models.Model):
    from_wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, related_name='transfer_from')
    to_wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, related_name='transfer_to')
    amount = models.FloatField()
    platform_profit = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.from_wallet.owner != self.to_wallet.owner:
                self.platform_profit = self.amount * settings.PLATFORM_TRANSFER_CHARGE
            self.from_wallet.bts -= self.amount + self.platform_profit
            if self.from_wallet.bts < 0:
                raise ValidationError('not enough bts')
            self.from_wallet.save(force_update=True, force_insert=False)
            self.to_wallet.bts += self.amount
            self.to_wallet.save(force_update=True, force_insert=False)
        return super(Transaction, self).save(*args, **kwargs)
