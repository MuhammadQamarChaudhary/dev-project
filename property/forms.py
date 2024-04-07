
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Property

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        
        """
        Form for user sign-up.
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class PropertyForm(forms.ModelForm):
    class Meta:
         
        """
        Form for adding a property.
        """
        model = Property
        fields = [
            'name', 'email', 'phone_no', 'price', 'listing_type',
            'area_in_sqft', 'no_of_rooms', 'no_of_bathrooms',
            'property_type', 'home_address', 'city', 'image'
        ]
class PropertyUpdateForm(forms.ModelForm):
    class Meta:

        """
        Form for updating a property.
         """

        model = Property
        fields = [
                    'name', 'email', 'phone_no', 'price', 'listing_type', 
                    'area_in_sqft', 'no_of_rooms', 'no_of_bathrooms', 
                    'property_type', 'home_address', 'city', 'image'
                ]