from rest_framework import serializers

from .models import InvoiceEntry, InvoiceEntryItem


class InvoiceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceEntry
        fields = '__all__'


class InvoiceEntryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceEntryItem
        fields = '__all__'
