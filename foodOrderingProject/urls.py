
from django.contrib import admin
from django.urls import path, include
from User.views import  GoogleLoginAPIView, UserInfoView, LogoutApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('User.urls')),
    # path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/', include('Restaurant.urls')),
    # path('api/', include('Admin.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('api/auth/google/', include('allauth.socialaccount.providers.google.urls')),
    # path('api/auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/auth/google/', GoogleLoginAPIView.as_view(), name='google-login'),
    path('api/auth/user/', UserInfoView.as_view(), name='user-info'),
    path('api/auth/logout/', LogoutApiView.as_view(), name='user-info'),

]
