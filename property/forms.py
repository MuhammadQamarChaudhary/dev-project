"""
Module for defining forms related to properties.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Property

class SignUpForm(UserCreationForm):
    """
    Form for user sign-up.
    """
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        """
        Form for adding a login.
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class PropertyForm(forms.ModelForm):
    """
    Form for adding a property.
    """
    class Meta:
        model = Property
        fields = [
            'name', 'email', 'phone_no', 'price', 'listing_type',
            'area_in_sqft', 'no_of_rooms', 'no_of_bathrooms',
            'property_type', 'home_address', 'city', 'image'
        ]

class PropertyUpdateForm(forms.ModelForm):
   
    """
    Form for updating a property.
    """
   
    class Meta:
        model = Property
        fields = [
            'name', 'email', 'phone_no', 'price', 'listing_type',
            'area_in_sqft', 'no_of_rooms', 'no_of_bathrooms',
            'property_type', 'home_address', 'city', 'image'
        ]
#the end of the code
