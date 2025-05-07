
from rest_framework import serializers
from .models import Restaurant

class RestaurantRegister(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'location', 'email', 'owner_name', 'password', 'role']
        
        