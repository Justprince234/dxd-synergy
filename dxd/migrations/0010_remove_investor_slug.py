# Generated by Django 4.1 on 2022-08-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dxd', '0009_investor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='slug',
        ),
    ]
