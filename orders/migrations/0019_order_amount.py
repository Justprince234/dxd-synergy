# Generated by Django 4.0.6 on 2022-07-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_remove_order_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.PositiveIntegerField(default=0.0),
        ),
    ]