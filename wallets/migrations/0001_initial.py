# Generated by Django 3.0.8 on 2020-07-28 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wallets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bts', models.PositiveIntegerField(default=1)),
                ('address', models.CharField(default=wallets.models.generate_wallet_address, max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
