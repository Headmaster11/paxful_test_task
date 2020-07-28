from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bts = models.PositiveIntegerField(default=1)
