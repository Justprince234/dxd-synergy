# Generated by Django 4.1 on 2022-08-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dxd', '0011_alter_investor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('message1', models.CharField(max_length=100)),
                ('message2', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Hompage Message',
            },
        ),
    ]
