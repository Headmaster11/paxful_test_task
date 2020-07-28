from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from bitcoin import pubtoaddr


def generate_wallet_address():
    return pubtoaddr(settings.BITKOIN_PUBLIC_KEY)


class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bts = models.PositiveIntegerField(default=1)
    address = models.CharField(max_length=100, default=generate_wallet_address)

    def save(self, *args, **kwargs):
        if self.id is None:
            if Wallet.objects.filter(owner=self.owner).count() >= 10:
                return False
        return super(Wallet, self).save(self)
