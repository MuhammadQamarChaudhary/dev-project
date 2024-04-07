"""
Module for defining URL patterns related to properties.
"""

from django.contrib import admin
from django.urls import path
from property import views

# Define URL patterns
urlpatterns = [
    path("", views.index, name='home'),
    path('signup',views.user_signup, name="SignUp"),
    path('login',views.user_login, name="login"),
    path('logout',views.user_logout, name="logout"),
    path("about", views.about, name='about'),
    path("addproperty", views.add_property, name='addprperty'),
    path("contact", views.contact, name='contact'),
    path("listing", views.property_listing, name='propertylisting'),
    path("mylisting", views.my_listing, name='mylisting'),
    path('delete_property/<str:property_name>/', views.delete_property, name='delete_property'),
    path('update_property/<str:property_name>/', views.update_property, name='update_property'),
]
