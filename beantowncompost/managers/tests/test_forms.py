from django.test import TestCase, Client
from django.urls import reverse
from managers.forms import (RequestManagerPermissionForm, GrantManagerPermissionForm,
UserRegisterForm, LoginForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm)
from dropoff_locations.models import DropoffLocation
from django.contrib.auth.models import User, AnonymousUser
#from managers.models import ManagerSitePermission
class TestPermissionForms(TestCase):
    def setUp(self):
        # create first user
        self.user1 = User.objects.create_user(
        username='test_ProjectManager')
        self.user1.set_password('SayCompost')

        # create first drop-off location
        self.dropoff1 = DropoffLocation.objects.create(
            neighborhood_name='Brighton',
            location_name='TestLocation1',
            location_description='This is a test site',
            location_address='123 fake st.',
            phone='123-456-7890',
            website='www.abc123.com',
            longitude='-71.05',
            latitude='42.1',
            city='Boston',
        )


    def test_request_manager_permission_form_valid_data(self):
        form = RequestManagerPermissionForm(data={
            'user': self.user1,
            'site': self.dropoff1,
            'status': 'requested',
            'notes': '',
        })
        self.assertTrue(form.is_valid())
    
    def test_request_manager_permission_form_no_data(self):
        form = RequestManagerPermissionForm(data={})
        self.assertFalse(form.is_valid())        
        self.assertEquals(len(form.errors), 2)

    def test_grant_manager_permission_form_valid_data(self):
        # check if form only accepts correct status choices
        form = RequestManagerPermissionForm(data={
            'user': self.user1,
            'site': self.dropoff1,
        })
        self.assertTrue(form.is_valid())
    
    def test_grant_manager_permission_form_no_data(self):
        form = GrantManagerPermissionForm(data={})
        self.assertFalse(form.is_valid())        
        self.assertEquals(len(form.errors), 3)

class TestRegistrationForm(TestCase):
    
    def test_user_registration_form_valid_data(self):
        """test that registering a user with a valid data works"""
        form = UserRegisterForm(data={
            'username': 'test_newuser1',
            'email': 'testuser@test.com',
            'password1': 'ThisIsAValidPassword952$!',
            'password2': 'ThisIsAValidPassword952$!',
        })
        self.assertTrue(form.is_valid())
    
    def test_user_registration_form_invalid_data(self):
        """test that registering a user with a weak password fails"""
        form = UserRegisterForm(data={
            'username': 'test_newuser1',
            'email': 'testuser@test.com',
            'password1': 'abc123', # weak password
            'password2': 'abc123', # weak password confirmation 
        })
        self.assertFalse(form.is_valid())

    def test_user_registration_form_no_data(self):
        """test that registering a user without providing data fails"""
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())

class TestLoginForm(TestCase):

    def test_login_form_valid_data(self):
        """test that valid logins from existing accounts works"""
        User.objects.create_user(username='test_newuser1', password='ThisIsAValidPassword952$!')
        form = LoginForm(data={
            'username': 'test_newuser1',
            'password': 'ThisIsAValidPassword952$!',
        })
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_data(self):
        """test that logging in from a non-existing account fails"""
        form = LoginForm(data={
            'username': 'test_newuser1',
            'password': 'ThisIsAValidPassword952$!',
        })
        self.assertFalse(form.is_valid())

    def test_login_form_no_data(self):
        """test that logging in without submitting data fails"""
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())

    def test_login_form_weak_password(self):
        """test that logging in from an account with a weak, unhashed password is invalid."""
        user = User.objects.create(username='test_newuser1', password='abc123') # weak password, not hashed
        form = LoginForm(data={
            'username': 'test_newuser1',
            'password': 'abc123', # weak password
        })
        self.assertFalse(form.is_valid())
        """test that logging in from an account with a weak, but hashed password is valid."""
        user.delete()
        User.objects.create_user(username='test_newuser1', password='abc123') # weak password, is hashed
        form = LoginForm(data={
            'username': 'test_newuser1',
            'password': 'abc123', # weak password
        })
        self.assertTrue(form.is_valid())

class TestPasswordChangeForm(TestCase):
    def setUp(self):
        # create first user
        self.user1 = User.objects.create_user(
        username='test_newuser1')
        self.user1.set_password('This!Is@A^Strong*Password?1234')
    
    def test_valid_password_change(self):
        """test that existing users can change their password to a new valid password"""
        form = PasswordChangeForm(self.user1, data={
            'old_password': 'This!Is@A^Strong*Password?1234',
            'new_password1': 'This!Is@A^Strong*Password?5678',
            'new_password2': 'This!Is@A^Strong*Password?5678',
        })
        self.assertTrue(form.is_valid())


            
    def test_invalid_password_change(self):
        """test that existing users cannot change their password to an invalid (weak) password"""
        form = PasswordChangeForm(self.user1, data={
            'old_password': 'This!Is@A^Strong*Password?1234',
            'new_password1': 'weak123',
            'new_password2': 'weak123',
        })
        self.assertFalse(form.is_valid())

class TestPasswordResetForm(TestCase):
    
    def test_valid_password_reset(self):
        """test that form allows valid email address constructions"""
        form = PasswordResetForm(data={
            'email': 'fake@email.com',
        })
        self.assertTrue(form.is_valid())
    
    def test_invalid_password_reset(self):
        """test that form doesn't allow invalid email address constructions"""
        form = PasswordResetForm(data={
            'email': 'fake@email',
        })
        self.assertFalse(form.is_valid())

class TestSetPasswordForm(TestCase):
    def setUp(self):
        # create first user
        self.user1 = User.objects.create_user(
        username='test_newuser1')
        self.user1.set_password('This!Is@A^Strong*Password?1234')

    def test_valid_password_set(self):
        form = SetPasswordForm(self.user1, data={
            'new_password1': 'This!Is@A^Strong*Password?5678',
            'new_password2': 'This!Is@A^Strong*Password?5678',
        })
        self.assertTrue(form.is_valid())
    
    def test_invalid_password_set(self):
         # weak password
        form = SetPasswordForm(self.user1, data={
            'new_password1': 'abc123',
            'new_password2': 'abc123',
        })
        self.assertFalse(form.is_valid())
        # non-matching passwords
        form = SetPasswordForm(self.user1, data={
            'new_password1': 'This!Is@A^Strong*Password?1234',
            'new_password2': 'This!Is@A^Strong*Password?5678',
        })
        self.assertFalse(form.is_valid())
