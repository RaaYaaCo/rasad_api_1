from rest_framework import serializers

from user.models import Store


class StoreSerializer(serializers.ModelSerializer):


    class Meta:
        model = Store
        fields = '__all__'


class StoreSearchSerializer(serializers.Serializer):
    search = serializers.CharField()
