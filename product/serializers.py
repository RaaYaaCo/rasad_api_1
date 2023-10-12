from rest_framework import serializers
from .models import ProductType, Unit, Degree, Product


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
