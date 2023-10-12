from rest_framework import serializers

from .models import User
from .validators import check_phone


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'u_code_meli', 'u_phone_number', 'password', 'is_active']


class UserCodeSerializer(serializers.Serializer):
    otp_code = serializers.CharField()



