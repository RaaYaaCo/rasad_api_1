from django.contrib import admin
from .models import InvoiceCustomer, InvoiceCustomerItem, ProductEntity

# Register your models here.


class InvoiceCustomerItemAdmin(admin.TabularInline):
    model = InvoiceCustomerItem
    raw_id_fields = ('p_id',)


@admin.register(InvoiceCustomer)
class InvoiceCustomerAdmin(admin.ModelAdmin):
    list_display = ['u_store_id', 'u_customer_id', 'ic_date_time']
    inlines = (InvoiceCustomerItemAdmin,)


@admin.register(ProductEntity)
class ProductEntityAdmin(admin.ModelAdmin):
    list_display = ['u_store_id', 'isi_id', 'p_id', 'sale_price', 'pe_is_active']
