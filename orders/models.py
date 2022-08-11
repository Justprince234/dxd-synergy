from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum
from django.conf import settings
import uuid
from django.urls import reverse
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

from dxd.models import Product
from coupons.models import Coupon
from cart import cart

# Create your models here.
choices = (('Received', 'Received'),
        ('Scheduled', 'Scheduled'), 
        ('Shipped', 'Shipped'),
        ('In Progress','In Progress'),
        )

# # Payment Method
# payment_choices = (
#     ('paystack', 'Paystack'),
#     ('pay_on_delivery', 'Pay on delivery')
#     )

class Order(models.Model):
    order_number = models.CharField(max_length=32, unique=True, null=False, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], editable=False)
    amount = models.PositiveIntegerField(default=0.00, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    payment_option = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length = 100, choices = choices, default="In Progress")
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    # def get_absolute_url(self):
    #     return reverse('orders:download', args=[self.id])


    def get_total_cost(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total = Decimal(total) - Decimal((self.discount / Decimal(100))) * Decimal(self.amount)
        return total

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def grand_total(self):
        """
        Override the original save method to set the grand total
        if it hasn't been set already.
        """
        final_total = 0
        final_total = Decimal(self.get_total_cost()) + Decimal(self.delivery_cost)
        return final_total

    # def save(self, *args, **kwargs):
    #     self.grand_total = self.amount + self.delivery_cost
    #     super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    

    def get_cost(self):
        return self.price * self.quantity
        
    def __str__(self):
        return f'Owned by {self.order.first_name}, Order number: {self.order.order_number}'

    def get_total_item_discount_price(self):
        return self.quantity * self.product.discount_price
    
    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_item_discount_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_item_discount_price()
        return self.get_total_item_price()