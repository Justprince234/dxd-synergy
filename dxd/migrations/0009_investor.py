# Generated by Django 4.1 on 2022-08-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dxd', '0008_product_best_seller_product_gift_product_new_arrival_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]