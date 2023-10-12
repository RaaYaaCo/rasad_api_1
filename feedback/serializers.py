from rest_framework import serializers

from .models import RatingStore, Complaint


class RatingStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingStore
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'


class StoreIdSerializer(serializers.Serializer):
    store_id = serializers.IntegerField()


class UserIdSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()





