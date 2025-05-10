

from django.urls import path, include
from .views import RestaurantDetailsViewSets, debugging
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurants', RestaurantDetailsViewSets, basename="restaurant")

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    # path('restaurants/', RestaurantDetailsViewSets.as_view({'get': 'list',    
    #     'post': 'create' }), name="restauarnt"),
    path("debug/", debugging )

]

print("Router URLs:", [str(url) for url in router.urls])