from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse

def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')

def order_payment(obj):
    url = obj.get_stripe_url()
    if obj.paid:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''
order_payment.short_description = 'Stripe payment'

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name_plural}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    
    # Filtra solo los campos que son instancias de Field
    fields = [field for field in opts.fields]
    
    # Escribe los nombres de las columnas
    writer.writerow([field.verbose_name for field in fields])
    
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name, None)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'address', 'postal_code', 'city', 'paid', order_payment, 'created', 'updated','get_total_cost', order_detail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]
