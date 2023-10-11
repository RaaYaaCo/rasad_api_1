from django.contrib import admin
from .models import InvoiceCustomer, InvoiceCustomerItem, ProductEntity

# Register your models here.


@admin.register(InvoiceCustomerItem)
class InvoiceCustomerItemAdmin(admin.ModelAdmin):
    list_display = ['p_id', 'iei_weight']
    raw_id_fields = ('p_id',)


@admin.register(InvoiceCustomer)
class InvoiceCustomerAdmin(admin.ModelAdmin):
    list_display = ['u_store_id', 'u_customer_id', 'ic_date_time']
    inlines = (InvoiceCustomerItem,)


@admin.register(ProductEntity)
class ProductEntityAdmin(admin.ModelAdmin):
    list_display = ['u_store_id', 'isi_is', 'p_id', 'sale_price', 'pe_is_active']
