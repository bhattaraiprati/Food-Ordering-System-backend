from django.db import models

# Create your models here.

class Restaurant(models.Model):

    restaurant_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    owner_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.restaurant_name

