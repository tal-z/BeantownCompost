from django.test import Client, TestCase
from django.urls import reverse, resolve
from dropoff_locations import views as dropoff_views 
from django.contrib.auth.models import User

class TestUrls(TestCase):

    def test_vote_url_resolves(self):
        url = reverse('vote')
        self.assertEqual(resolve(url).func, dropoff_views.vote)
    
    def test_add_location_url_resolves(self):
        url = reverse('add_location')
        self.assertEqual(resolve(url).func, dropoff_views.add_location)

    def test_suggest_location_url_resolves(self):
        url = reverse('suggest_location')
        self.assertEqual(resolve(url).func, dropoff_views.suggest_location)

    def test_correct_location_url_resolves(self):
        url = reverse('correct_location')
        self.assertEqual(resolve(url).func, dropoff_views.correct_location)

    def test_update_location_url_resolves(self):
        url = reverse('update_location')
        self.assertEqual(resolve(url).func, dropoff_views.update_location)

    def test_update_site_managers_url_resolves(self):
        url = reverse('update_site_managers')
        self.assertEqual(resolve(url).func, dropoff_views.update_site_managers)

    def test_request_management_permission_url_resolves(self):
        url = reverse('request_management_permission')
        self.assertEqual(resolve(url).func, dropoff_views.request_management_permission)
    
    def test_review_suggested_locations_url_resolves(self):
        url = reverse('review_suggested_locations')
        self.assertEqual(resolve(url).func, dropoff_views.review_suggested_locations)
    
    def test_review_suggested_corrections_url_resolves(self):
        url = reverse('review_suggested_corrections')
        self.assertEqual(resolve(url).func, dropoff_views.review_suggested_corrections)
    
    def test_locations_url_resolves(self):
        url = reverse('locations')
        self.assertEqual(resolve(url).func, dropoff_views.locations)