
from rest_framework import serializers
from .models import Restaurant
from django.contrib.auth.hashers import make_password


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'location', 'email', 'owner_name', 'password', 'role', "status"]
        
    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)