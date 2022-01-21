from django.forms import ModelForm
from .models import DropoffLocation, AddDropoffLocation, CorrectDropoffLocation, VoteDropoffLocation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field

class DropoffLocationForm(ModelForm):
    class Meta:
        model = DropoffLocation
        fields = ['neighborhood_name','location_name','location_description','location_address','phone','url','x','y', 'city']

class AddDropoffLocationForm(ModelForm):
    class Meta:
        model = AddDropoffLocation
        fields = ['neighborhood_name','location_name','location_description','location_address','phone','url','x','y', 'city']


class CorrectDropoffLocationForm(ModelForm):
    class Meta:
        model = CorrectDropoffLocation
        fields = ['neighborhood_name','location_name','location_description','location_address','phone','url','x','y', 'city']


class VoteDropoffLocationForm(ModelForm):
    class Meta:
        model = VoteDropoffLocation
        fields = ['first_name','last_name','email','zip', 'x','y']
        