# Generated by Django 3.2.3 on 2021-05-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='market_value',
            field=models.PositiveIntegerField(default=1000000),
        ),
        migrations.AlterField(
            model_name='team',
            name='bank_balance',
            field=models.PositiveIntegerField(default=5000000),
        ),
    ]