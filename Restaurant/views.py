from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import RestaurantSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def restaurentDetails():
    return None

@api_view(['POST'])
def Restaurant_Register(request):
    print("upto here")
    serializer = RestaurantSerializer(data=request.data)
    print("Passed level 2")
    if serializer.is_valid():
        serializer.save()
        return Response({"success": "Register Successfully"}, status=status.HTTP_201_CREATED)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
