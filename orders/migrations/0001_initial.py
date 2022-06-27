# Generated by Django 4.0.5 on 2022-06-24 17:16

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dxd', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(default='US', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('braintree_id', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='dxd.product')),
            ],
        ),
    ]