from rest_framework import serializers
from user.models import Users


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = [
            'id', 'first_name', 'last_name', 'username',
            'password', 'email', 'phone_number', 'emergency_number',
            'national_code', 'birth_certificate_id', 'address',
            'province', 'city', 'address', 'home_number', 'postcode'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = []
