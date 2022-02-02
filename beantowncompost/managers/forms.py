from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Column, Submit
from crispy_forms.bootstrap import FormActions


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            
            self.helper.layout = Layout(
                Div('email', 'username',
                    Column('password1', css_class="col-6"), 
                    Column('password2', css_class="col-6"), css_class='row'),
                FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3'))
)


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'login-form'

        #self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div('username', placeholder="Username",  css_class="row mt-2"),
            Div('password', placeholder="Password",  css_class="row mt-2"),
            FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3 mb-3'))
        )


class PasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'reset-form'

        #self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div('old_password', placeholder="Old Password",  css_class="row mt-2"),
            Div('new_password1', placeholder="New Password",  css_class="row mt-2"),
            Div('new_password2', placeholder="Confirm New Password",  css_class="row mt-2"),
            FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3 mb-3'))
        )

class PasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'reset-form'

        #self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div('email', placeholder="email address",  css_class="row mt-2"),
            FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3 mb-3'))
        )

class SetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'reset-form'

        #self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div('new_password1', placeholder="New Password",  css_class="row mt-2"),
            Div('new_password2', placeholder="Confirm New Password",  css_class="row mt-2"),
            FormActions(Submit('Submit', 'Submit', css_class='btn btn-light mt-3 mb-3'))
        )