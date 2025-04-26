
from django.contrib import admin
from django.urls import path, include
from User.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('User.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/', include('Restaurant.urls')),
    # path('api/', include('Admin.urls')),

]
