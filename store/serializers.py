from rest_framework import serializers

from user.models import Store


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = 's_slug'


class StoreSearchSerializer(serializers.Serializer):
    search = serializers.CharField()
