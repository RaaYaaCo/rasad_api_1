from rest_framework import serializers

from .models import InvoiceCustomer, InvoiceCustomerItem, ProductEntity
from user.serializers import WholesalerStoreInvoiceSerializer, UserInvoiceSerializer
from product.serializers import ProductSerializers
from invoice_sales.serializers import InvoiceSalesSerializer


class InvoiceCustomerAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceCustomer
        fields = '__all__'


class InvoiceCustomerItemAddSerializer(serializers.ModelSerializer):
    u_store_id = WholesalerStoreInvoiceSerializer(read_only=True)
    isi_id = InvoiceSalesSerializer(read_only=True)
    p_id = ProductSerializers(read_only=True)

    class Meta:
        model = InvoiceCustomerItem
        fields = '__all__'


class ProductEntitySerializer(serializers.ModelSerializer):
    p_id = ProductSerializers(read_only=True)

    class Meta:
        model = ProductEntity
        fields = ['u_store_id', 'isi_id', 'p_id', 'isi_price', 'sale_price', 'pe_weight', 'pe_is_active', 'pe_date_time', 'pe_update_time']


class InvoiceCustomerSerializer(serializers.ModelSerializer):
    u_store_id = WholesalerStoreInvoiceSerializer(read_only=True)
    u_customer_id = UserInvoiceSerializer(read_only=True)

    class Meta:
        model = InvoiceCustomer
        fields = ['id', 'u_store_id', 'u_customer_id', 'ic_date_time']


class InvoiceCustomerItemSerializer(serializers.ModelSerializer):
    p_id = ProductSerializers(read_only=True)
    pe_id = ProductEntitySerializer(read_only=True)

    class Meta:
        model = InvoiceCustomerItem
        fields = ['id', 'ic_id', 'p_id', 'ici_weight', 'pe_id']
