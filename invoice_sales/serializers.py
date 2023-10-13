from rest_framework import serializers

from .models import InvoiceSales, InvoiceSalesItem
from user.serializers import UserSerializer
from product.serializers import ProductSerializers, ProductPriceSerializer


class InvoiceSalesAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceSales
        fields = '__all__'


class InvoiceSalesItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceSalesItem
        fields = '__all__'


class InvoiceSalesSerializer(serializers.ModelSerializer):
    u_wholesaler_id = UserSerializer(read_only=True)
    u_store_id = UserSerializer(read_only=True)

    class Meta:
        model = InvoiceSales
        fields = ['id',
                  'u_wholesaler_id',
                  'u_store_id',
                  'is_date_time'
                  ]


class InvoiceSalesItemSerializer(serializers.ModelSerializer):
    p_id = ProductSerializers(read_only=True)
    pp_id = ProductPriceSerializer(read_only=True)

    class Meta:
        model = InvoiceSalesItem
        fields = ['id', 'is_id', 'p_id', 'isi_weight', 'pp_id']
