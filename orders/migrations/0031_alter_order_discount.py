# Generated by Django 4.1 on 2022-08-10 01:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_remove_order_grand_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]