from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializers, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView



# Create your views here.
def loginDetails():
    return None

class loginAndRegistration(APIView):

    def post(self, request):
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.error_messages)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def UserRegister(request):
    print(request.data)
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserViewSet(ModelViewSet):

    serializer_class = UserSerializers
    queryset = User.objects.all()


# class LoginDetails(ModelViewSet):

#     permission_classes = [IsAuthenticated]

#     def retrieve(self, request ):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         return 

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:5173"  # Your frontend URL
    client_class = OAuth2Client