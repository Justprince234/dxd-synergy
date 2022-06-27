from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name','phone', 'email', 'address', 'postal_code', 'state', 'country', 'paid','created']
    list_filter = ['id','paid', 'created', 'state', 'country']
    inlines = [OrderItemInline]