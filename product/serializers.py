from rest_framework import serializers
from .models import ProductType, Unit, Degree, Product, ProductPrice


class ProductTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = '__all__'


class DegreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Degree
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPrice
        fields = '__all__'
