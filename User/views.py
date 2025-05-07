from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializers, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import status, permissions
import requests


User = get_user_model()


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



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = "http://localhost:5173"  # Your frontend URL
#     client_class = OAuth2Client

#     def post(self, request, *args, **kwargs):
#         try:
#             return super().post(request, *args, **kwargs)
#         except Exception as e:
#             # Add better error handling
#             print(f"Google login error: {str(e)}")
#             return Response(
#                 {"error": "Something went wrong with Google authentication. Please try again."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

class GoogleLoginAPIView(APIView):
    def post(self, request):
        id_token = request.data.get("id_token")
        if not id_token:
            return Response({"error": "ID token is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Verify token with Google
        google_response = requests.get(
            f"https://oauth2.googleapis.com/tokeninfo?id_token={id_token}"
        )

        if google_response.status_code != 200:
            return Response({"error": "Invalid ID token"}, status=status.HTTP_400_BAD_REQUEST)

        user_info = google_response.json()
        email = user_info.get("email")
        name = user_info.get("name")

        if not email:
            return Response({"error": "Email not available in token"}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(
            email=email,
            defaults={"name": name}
        )
        if created:
            user.role = 'user'
            user.save()

        # token, _ = Token.objects.get_or_create(user=user)
        refresh = CustomTokenObtainPairSerializer.get_token(user)

        return Response({"access": str(refresh.access_token),
            "refresh": str(refresh),})

class UserInfoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return user information"""
        user = request.user
        data = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        
        # Add profile picture URL if available
        try:
            if hasattr(user, 'profile_picture') and user.profile_picture:
                data['profile_picture'] = user.profile_picture
        except:
            pass

        # Add any social account info
        try:
            social_account = user.socialaccount_set.first()
            if social_account:
                data.update({
                    'provider': social_account.provider,
                    'name': social_account.extra_data.get('name', ''),
                    'picture': social_account.extra_data.get('picture', ''),
                })
        except:
            pass
            
        return Response(data)
    
class LogoutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"details": "Logout Successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        