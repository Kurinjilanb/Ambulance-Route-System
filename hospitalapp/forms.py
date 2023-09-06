from django import forms
from .models import Hospital
from .models import Location
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    """
    UserForm is used to create a form for the User model
    """
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']




class HospitalForm(forms.ModelForm):
    """
    HospitalForm is used to create a form for the Hospital model
    """
    class Meta:
        model = Hospital
        fields = ['name', 'beds_available']

class LocationForm(forms.ModelForm):
    """
    LocationForm is used to create a form for the Location model
    """
    class Meta:
        model = Location
        fields = ['name', 'address', 'latitude', 'longitude']

