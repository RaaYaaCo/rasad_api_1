from rest_framework import serializers

from .models import InvoiceCustomer, InvoiceCustomerItem, ProductEntity
from user.serializers import WholesalerStoreInvoiceSerializer, UserInvoiceSerializer
from product.serializers import ProductSerializers


class InvoiceCustomerAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceCustomer
        fields = '__all__'


class InvoiceCustomerItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceCustomerItem
        fields = '__all__'


class ProductEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEntity
        fields = '__all__'


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
