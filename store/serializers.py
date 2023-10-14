from rest_framework import serializers

from user.models import Store, User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    u_id = UserDetailSerializer(read_only=True)

    class Meta:
        model = Store
        fields = '__all__'


class StoreSearchSerializer(serializers.Serializer):
    search = serializers.CharField()
