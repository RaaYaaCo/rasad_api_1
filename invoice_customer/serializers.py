from rest_framework import serializers
from .models import InvoiceCustomer, InvoiceCustomerItem


class InvoiceCustomerAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceCustomer
        fields = '__all__'


class InvoiceCustomerItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceCustomerItem
        fields = '__all__'
