# Generated by Django 4.1 on 2022-08-10 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_alter_order_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='grand_total',
        ),
    ]
