from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Order, OrderItem

import csv
import datetime

admin.site.site_header = 'DXD SYNERGY'
admin.site.site_title = 'DXD SYNERGY'
admin.site.index_title = 'DXD SYNERGY ADMIN'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not
              field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'

def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')

def order_pdf(obj):
    url = reverse('orders:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')

order_pdf.short_description = 'Invoice'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'first_name', 'phone','status', 'paid', order_detail, order_pdf]
    list_filter = ['id','paid', 'status', 'state', 'country']
    inlines = [OrderItemInline]
    actions = [export_to_csv]