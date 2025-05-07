

from django.urls import path
from .views import *

urlpatterns = [
    path("", restaurentDetails ),
    path("restaurant/register", RestaurantRegister )

]
