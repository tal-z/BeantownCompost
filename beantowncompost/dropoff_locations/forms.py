from turtle import onclick
from django.forms import ModelForm
from .models import DropoffLocation, AddDropoffLocation, CorrectDropoffLocation, VoteDropoffLocation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Column, Submit
from crispy_forms.bootstrap import FormActions

class DropoffLocationForm(ModelForm):
    class Meta:
        model = DropoffLocation
        fields = ['location_name','location_description','location_address', 'neighborhood_name', 'city', 'phone','website','longitude','latitude']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            
            self.helper.layout = Layout(
                Div(Column('location_name', css_class='col-4'), Column('location_address', css_class='col-8'), css_class='row'),
                'location_description',
                Div(Column('neighborhood_name', css_class='col-6'), Column('city', css_class='col-6'), css_class='row'),
                Div(Column('phone', css_class='col-4'), Column('website', css_class='col-8'), css_class='row'),
                'longitude',
                'latitude',
                FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3'))
            )
class AddDropoffLocationForm(ModelForm):
    class Meta:
        model = AddDropoffLocation
        fields = ['location_name','location_description','location_address', 'neighborhood_name', 'city', 'phone','website','longitude','latitude']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(Column('location_name', css_class='col-4'), Column('location_address', css_class='col-8'), css_class='row'),
            'location_description',
            Div(Column('neighborhood_name', css_class='col-6'), Column('city', css_class='col-6'), css_class='row'),
            Div(Column('phone', css_class='col-4'), Column('website', css_class='col-8'), css_class='row'),
            'longitude',
            'latitude',
            FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3'))
        )
        


class CorrectDropoffLocationForm(ModelForm):
    class Meta:
        model = CorrectDropoffLocation
        fields = ['location_name','location_description','location_address', 'neighborhood_name', 'city', 'phone','website','longitude','latitude']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        
        self.helper.layout = Layout(
            Div(Column('location_name', css_class='col-4'), Column('location_address', css_class='col-8'), css_class='row'),
            'location_description',
            Div(Column('neighborhood_name', css_class='col-6'), Column('city', css_class='col-6'), css_class='row'),
            Div(Column('phone', css_class='col-4'), Column('website', css_class='col-8'), css_class='row'),
            'longitude',
            'latitude',
            FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3'))
        )


class VoteDropoffLocationForm(ModelForm):
    class Meta:
        model = VoteDropoffLocation
        fields = ['first_name','last_name','email','zip', 'longitude','latitude']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(Column('first_name', css_class='col-6'), Column('last_name', css_class='col-6'), css_class='row'),
            'email',
            'zip',
            'longitude',
            'latitude',
            FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3', onclick='validate_latlng()'))
        )