from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bts = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.id is None:
            if Wallet.objects.filter(owner=self.owner).count() >= 10:
                return False
        return super(Wallet, self).save(self)
