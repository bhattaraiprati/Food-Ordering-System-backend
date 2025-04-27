
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name' ,'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    username_field = 'email'

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')

        data = super().validate({'email': user.email, 'password': password})  # trick super to work
        data['email'] = user.email
        data['name'] = user.name
        data['role'] = user.role
        data['id'] = user.id
        return data
