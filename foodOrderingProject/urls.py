
from django.contrib import admin
from django.urls import path, include
from User.views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('User.urls')),
    # path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/', include('Restaurant.urls')),
    # path('api/', include('Admin.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('api/auth/google/', include('allauth.socialaccount.providers.google.urls')),
    path('api/auth/google/', GoogleLogin.as_view(), name='google_login'),

]
