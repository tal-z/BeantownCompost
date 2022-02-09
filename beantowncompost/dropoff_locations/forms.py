
from django.forms import ModelForm, IntegerField, HiddenInput
from .models import DropoffLocation, SuggestDropoffLocation, CorrectDropoffLocation, VoteDropoffLocation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Column, Submit
from crispy_forms.bootstrap import FormActions

class DropoffLocationForm(ModelForm):
    id = IntegerField()
    class Meta:
        model = DropoffLocation
        fields = ['id', 'location_name','location_description','location_address', 'neighborhood_name', 'city', 'phone','website','longitude','latitude']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.fields['id'].widget = HiddenInput()
            self.helper.form_action = "/add_location/"

            self.helper.layout = Layout(
                Div('id'),
                Div(Column('location_name', css_class='col-4'), Column('location_address', css_class='col-8'), css_class='row'),
                'location_description',
                Div(Column('neighborhood_name', css_class='col-6'), Column('city', css_class='col-6'), css_class='row'),
                Div(Column('phone', css_class='col-4'), Column('website', css_class='col-8'), css_class='row'),
                'longitude',
                'latitude',
                FormActions(Submit('Submit', 'Add Location', onclick='validate_latlng()', css_class='btn btn-light mt-3'))
            )
            

class UpdateDropoffLocationForm(ModelForm):
    id = IntegerField()
    class Meta:
        model = DropoffLocation
        fields = ['id', 'location_name','location_description','location_address', 'neighborhood_name', 'city', 'phone','website','longitude','latitude']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.fields['id'].widget = HiddenInput()
            self.helper.form_action = "/update_location/"

            self.helper.layout = Layout(
                Div('id'),
                Div(Column('location_name', css_class='col-4'), Column('location_address', css_class='col-8'), css_class='row'),
                'location_description',
                Div(Column('neighborhood_name', css_class='col-6'), Column('city', css_class='col-6'), css_class='row'),
                Div(Column('phone', css_class='col-4'), Column('website', css_class='col-8'), css_class='row'),
                'longitude',
                'latitude',
                FormActions(Submit('Submit', 'Update Location', onclick='validate_latlng()', css_class='btn btn-light mt-3'))
            )

class SuggestDropoffLocationForm(ModelForm):

    class Meta:
        model = SuggestDropoffLocation
        fields = ['first_name', 'last_name', 'location_name','location_description','location_address', 'neighborhood_name', 'city', 'phone','website','longitude','latitude']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(Column('first_name', css_class='col-6'), Column('last_name', css_class='col-6'), css_class='row'),
            Div(Column('location_name', css_class='col-4'), Column('location_address', css_class='col-8'), css_class='row'),
            'location_description',
            Div(Column('neighborhood_name', css_class='col-6'), Column('city', css_class='col-6'), css_class='row'),
            Div(Column('phone', css_class='col-4'), Column('website', css_class='col-8'), css_class='row'),
            'longitude',
            'latitude',
            FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3', onclick='validate_latlng()'))
        )
        

class ReviewSuggestDropoffForm(ModelForm):
    id = IntegerField()

    class Meta:
        model = SuggestDropoffLocation
        fields = ['id', 'location_name','location_description','location_address', 'neighborhood_name', 'city', 'phone','website','longitude','latitude']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(Column('id', css_class='col-6'), css_class='row'),
            Div(Column('location_name', css_class='col-4'), Column('location_address', css_class='col-8'), css_class='row'),
            'location_description',
            Div(Column('neighborhood_name', css_class='col-6'), Column('city', css_class='col-6'), css_class='row'),
            Div(Column('phone', css_class='col-4'), Column('website', css_class='col-8'), css_class='row'),
            'longitude',
            'latitude',
            Div(
                FormActions(
                    Submit('add-site', 'Add Site to Map', css_class='btn btn-success mt-3', onclick='validate_latlng()'),
                    Submit('remove-from-queue', 'Remove Site from Suggestion Queue', css_class='btn btn-danger mt-3')
                ), css_class='col-6'),
            )


class CorrectDropoffLocationForm(ModelForm):
    id = IntegerField()
    class Meta:
        model = CorrectDropoffLocation
        fields = ['id', 'first_name', 'last_name', 'location_name','location_description','location_address', 'neighborhood_name', 'city', 'phone','website','longitude','latitude']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.fields['id'].widget = HiddenInput()

        self.helper.layout = Layout(
            Div('id'),
            Div(Column('first_name', css_class='col-6'), Column('last_name', css_class='col-6'), css_class='row'),
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