# Generated by Django 3.0.8 on 2020-07-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_auto_20200728_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='bts',
            field=models.DecimalField(decimal_places=8, default=1, max_digits=30),
        ),
    ]
