from rest_framework import serializers

from .models import InvoiceEntry, InvoiceEntryItem
from user.serializers import UserSerializer
from product.serializers import ProductSerializers


class InvoiceEntryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceEntry
        fields = '__all__'


class InvoiceEntryItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceEntryItem
        fields = '__all__'


class InvoiceEntrySerializer(serializers.ModelSerializer):
    u_wholesaler_id = UserSerializer(read_only=True)

    class Meta:
        model = InvoiceEntry
        fields = ['id',
                  'u_wholesaler_id',
                  'ie_driver',
                  'ie_full_weight',
                  'ie_empty_weight',
                  'ie_total_weight',
                  'ie_date_time'
                  ]


class InvoiceEntryItemSerializer(serializers.ModelSerializer):
    p_id = ProductSerializers()

    class Meta:
        model = InvoiceEntryItem
        fields = ['id', 'ie_id', 'p_id', 'iei_weight']
