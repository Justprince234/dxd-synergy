# Generated by Django 4.0.6 on 2022-07-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_order_coupon_order_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Received', 'Received'), ('Scheduled', 'Scheduled'), ('Shipped', 'Shipped'), ('In Progress', 'In Progress')], default='In Progress', max_length=100),
        ),
    ]