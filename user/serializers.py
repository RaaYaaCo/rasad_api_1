from django.core.exceptions import ValidationError
from django.contrib.gis.geos import GEOSGeometry

from rest_framework import serializers
from rest_framework_gis.serializers import GeometryField

from .models import User, Store


class UserSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(label='password')
    password_2 = serializers.CharField(label="confirm password")

    class Meta:
        model = User
        fields = ['id',
                  'first_name',
                  'last_name',
                  'u_code_meli',
                  'u_phone_number',
                  'password_1',
                  'password_2',
                  'is_active']
        read_only_fields = ['is_active']

    def validate(self, data):
        password_1_value = data.get('password_1')
        password_2_value = data.get('password_2')
        if password_1_value and password_2_value and password_1_value != password_2_value:
            raise ValidationError("The passwords must match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        u_code_meli=validated_data['u_code_meli'],
                                        u_phone_number=validated_data['u_phone_number'],
                                        password=validated_data['password_1'])
        return user

# ----------------


class UserCodeSerializer(serializers.Serializer):
    otp_code = serializers.CharField(required=True)

# ----------------------------------------------------------------------------


class WholesalerStoreSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    code_meli = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    password_1 = serializers.CharField(required=True, label='password')
    password_2 = serializers.CharField(required=True, label='confirm password')
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    location = GeometryField(required=True)  # required=True
    license = serializers.CharField(required=True)
    postal_code = serializers.CharField(required=True)

    def validate(self, data):
        password_1_value = data.get('password_1')
        password_2_value = data.get('password_2')
        if password_1_value and password_2_value and password_1_value != password_2_value:
            raise ValidationError("The passwords must match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        u_code_meli=validated_data['code_meli'],
                                        u_phone_number=validated_data['phone_number'],
                                        password=validated_data['password_1'])

        location = GEOSGeometry(validated_data['location'])
        store = Store.objects.create(u_id=user,
                                     s_name=validated_data['name'],
                                     s_description=validated_data['description'],
                                     s_license=validated_data['license'],
                                     s_postal_code=validated_data['postal_code'],
                                     s_address=validated_data['address'],
                                     s_location=location,
                                     )
        return store

# -----------------


class WholesalerStoreCodeSerializer(serializers.Serializer):
    otp_code = serializers.CharField(required=True)

# ----------------------------------------------------------------------------


class OtherSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(label='password')
    password_2 = serializers.CharField(label="confirm password")
    group = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id',
                  'first_name',
                  'last_name',
                  'u_code_meli',
                  'u_phone_number',
                  'password_1',
                  'password_2',
                  'group',
                  'is_active']
        read_only_fields = ['is_active']

    def validate(self, data):
        password_1_value = data.get('password_1')
        password_2_value = data.get('password_2')
        if password_1_value and password_2_value and password_1_value != password_2_value:
            raise ValidationError("The passwords must match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        u_code_meli=validated_data['code_meli'],
                                        u_phone_number=validated_data['phone_number'],
                                        password=validated_data['password_1'],
                                        group=validated_data['group'])
        return user

# ----------------


class OtherCodeSerializer(serializers.Serializer):
    otp_code = serializers.CharField(required=True)
