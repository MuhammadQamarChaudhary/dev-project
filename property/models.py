"""
Module for defining property models.
"""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    listing_type = models.CharField(max_length=50)
    area_in_sqft = models.CharField(max_length=50)
    no_of_rooms = models.IntegerField()
    no_of_bathrooms = models.IntegerField()
    property_type = models.CharField(max_length=100)
    home_address = models.TextField()
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')  # Specifies directory within MEDIA_ROOT

    def __str__(self):
        return self.name