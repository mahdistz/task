from rest_framework import serializers
from user.models import Users, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['province', 'city', 'address', 'home_number', 'postcode']


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'username', 'email',
                  'phone_number', 'emergency_number', 'birth_certificate_id',
                  ]
