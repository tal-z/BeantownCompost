from django.test import TestCase
from managers.forms import RequestManagerPermissionForm
from dropoff_locations.models import DropoffLocation
from django.contrib.auth.models import User
from managers.models import ManagerSitePermission

class TestForms(TestCase):
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