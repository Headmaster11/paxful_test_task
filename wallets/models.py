from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

from bitcoin import random_key, privtopub, pubtoaddr


def generate_wallet_address():
    my_private_key = random_key()
    my_public_key = privtopub(my_private_key)
    return pubtoaddr(my_public_key)


class Wallet(models.Model):
    address = models.CharField(max_length=100, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bts = models.DecimalField(default=1, max_digits=30, decimal_places=8)

    def save(self, *args, **kwargs):
        if self.pk == '':
            if Wallet.objects.filter(owner=self.owner).count() >= 10:
                raise ValidationError('max number of wallets')
            self.pk = generate_wallet_address()
        return super(Wallet, self).save(*args, **kwargs)

    def __str__(self):
        return self.address
