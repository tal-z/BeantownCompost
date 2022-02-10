from multiprocessing import Manager
from operator import le
from django.test import TestCase
from managers.models import ManagerSitePermission, SITEMANAGER_STATUSES
from dropoff_locations.models import DropoffLocation
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
class TestModels(TestCase):

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

        # Create first manager site permission
        self.permission1 = ManagerSitePermission.objects.create(
            user=self.user1,
            site=self.dropoff1
        )

    
    def test_no_dupes_in_management_site_permissions(self):
        # check that list and set are same size (no dupes)
        permissions = ManagerSitePermission.objects.all()
        self.assertEqual(len(permissions), len(set(permissions)))
        # check that attempting to add a dupe throws an exception
        with self.assertRaises(IntegrityError) as context:
            ManagerSitePermission.objects.create(
                user=self.user1,
                site=self.dropoff1
            )
        self.assertTrue('duplicate key value violates unique constraint' in str(context.exception))
    
        
    def test_site_permissions_statuses_allowed(self):
        # Check that status is being set on create
        self.assertTrue(self.permission1.status in [status[0] for status in SITEMANAGER_STATUSES])



