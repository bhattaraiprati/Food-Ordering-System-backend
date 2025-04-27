
from django.urls import path, include
from .views import UserViewSet, UserRegister
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView



router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

# urlpatterns = router.urls 


urlpatterns = [
    # path('', include(router.urls)),
    path('userRegister/', UserRegister, name="userRegister"),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]