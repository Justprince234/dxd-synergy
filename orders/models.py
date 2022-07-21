from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum
from django.conf import settings
import uuid
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

from dxd.models import Product
from coupons.models import Coupon

# Create your models here.
choices = (('Received', 'Received'),
        ('Scheduled', 'Scheduled'), 
        ('Shipped', 'Shipped'),
        ('In Progress','In Progress'),
        )

class Order(models.Model):
    order_number = models.CharField(max_length=32, unique=True, null=False, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = CountryField(multiple=False, blank_label='(select country)', default="NIG")
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length = 100, choices = choices, default="In Progress")
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total = total - float((self.coupon.discount / Decimal(100))) * order_item.get_final_price()
        return total

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    # def update_total(self):
    #     """
    #     Update grand total each time a line item is added,
    #     accounting for delivery costs.
    #     """
    #     self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
    #     if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
    #         self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
    #     else:
    #         self.delivery_cost = 0
    #     self.grand_total = self.order_total + self.delivery_cost
    #     self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

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