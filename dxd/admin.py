from django.contrib import admin

# Register your models here.
from .models import (
    Category,
    Product
)

admin.site.site_header = 'DXD SYNERGY'
admin.site.site_title = 'DXD SYNERGY'
admin.site.index_title = 'DXD SYNERGY ADMIN'

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'price', 'discount_price', 'available', 'description')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Product, ProductAdmin)