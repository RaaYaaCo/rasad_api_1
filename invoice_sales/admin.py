from django.contrib import admin
from .models import InvoiceSales, InvoiceSalesItem

# Register your models here.


@admin.register(InvoiceSalesItem)
class InvoiceSalesItemAdmin(admin.ModelAdmin):
    list_display = ['p_id', 'iei_weight']
    raw_id_fields = ('p_id',)


@admin.register(InvoiceSales)
class InvoiceSalesAdmin(admin.ModelAdmin):
    list_display = ['u_wholesaler_id', 'u_store_id', 'ie_date_time']
    inlines = (InvoiceSalesItem,)
