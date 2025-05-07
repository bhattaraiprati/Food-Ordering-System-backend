from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import RestaurantRegister
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def restaurentDetails():
    return None

@api_view(['POST'])
def RestaurantRegister(self, request, *args, **kwargs):

    serializer = RestaurantRegister(data= request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"success": "Register Successfully"}, status=status.HTTP_201_CREATED)
    return Response({'error': serializer.error}, status=status.HTTP_400_BAD_REQUEST)
