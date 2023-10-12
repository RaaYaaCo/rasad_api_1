from django.contrib import admin
from .models import InvoiceSales, InvoiceSalesItem

# Register your models here.


class InvoiceSalesItemAdmin(admin.TabularInline):
    model = InvoiceSalesItem
    raw_id_fields = ('p_id',)


@admin.register(InvoiceSales)
class InvoiceSalesAdmin(admin.ModelAdmin):
    list_display = ['u_wholesaler_id', 'u_store_id', 'is_date_time']
    inlines = (InvoiceSalesItemAdmin,)
