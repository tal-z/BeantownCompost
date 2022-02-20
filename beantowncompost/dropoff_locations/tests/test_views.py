from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from dropoff_locations.models import DropoffLocation
from managers.models import ManagerSitePermission
from django.contrib.messages import get_messages

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_ProjectManager')
        self.user.set_password('SayCompost')
        self.user.save()
        self.client = Client()
        self.client.login(username="test_ProjectManager", password="SayCompost")
        data = {
            'location_name': 'test',
            'location_address': 'test',
            'location_description': 'test',
            'neighborhood_name': 'test',
            'city': 'test',
            'phone': '1-(123)-456.7890',
            'website': 'www.test.com',
            'longitude': -71,
            'latitude': 43,
        }
        self.dropoff = DropoffLocation.objects.create(**data)

    def test_index_GET(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_index_POST(self):
        response = self.client.post(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/index.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_vote_GET(self):
        response = self.client.post(reverse('vote'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/vote.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_vote_POST(self):
        
        # First assert that submitting an empty form returns the vote page 
        response = self.client.post(reverse('vote'), data={})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/vote.html')
        self.assertTemplateUsed(response, 'base.html')
        # Next, assert that submitting an invalid form also returns the vote page 
        response = self.client.post(reverse('vote'), data={
            'first_name': 'test',
            'last_name': 'test',
            'email': 'fake@email',
            'zip': 12345, # incorrectly formatted email, plus missing fields
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/vote.html')
        self.assertTemplateUsed(response, 'base.html')
        # last, assert that submitting a valid form returns the thanks page 
        response = self.client.post(reverse('vote'), data={
            'first_name': 'test',
            'last_name': 'test',
            'email': 'fake@email.com',
            'zip': 12345,
            'longitude': -71,
            'latitude': 42,
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/thanks.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_suggest_location_GET(self):
        response = self.client.get(reverse('suggest_location'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/suggest_location.html')
    
    def test_suggest_location_POST(self):
        # check that an empty/invalid form does not save, and instead returns the suggest_location template
        response = self.client.post(reverse('suggest_location'), data={})
        self.assertTemplateUsed(response, 'dropoff_locations/suggest_location.html')
        response = self.client.post(reverse('suggest_location'), data={
            'first_name': 'tal',
            'last_name': 'zaken'
        })
        self.assertTemplateUsed(response, 'dropoff_locations/suggest_location.html')
        # check that a valid form returns the thanks template
        response = self.client.post(reverse('suggest_location'), data={
            'first_name': 'tal',
            'last_name': 'zaken',
            'location_name': 'test',
            'location_address': 'test',
            'location_description': 'test',
            'neighborhood_name': 'test',
            'city': 'test',
            'phone': '1-(123)-456.7890',
            'website': 'www.test.com',
            'longitude': -71,
            'latitude': 43,
        })
        self.assertTemplateUsed(response, 'dropoff_locations/thanks.html')

    def test_correct_location_unauthenticated_GET(self):
        # check that visiting the route without supplying a param redirects to the locations page and displays a message
        self.client.logout()
        response = self.client.get(reverse('correct_location'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'dropoff_locations/correct_location.html')
        # check that visiting the route with a valid param returns the correct_location template
        response = self.client.get(reverse('correct_location'), {'id': 3})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/correct_location.html')

    def test_correct_location_authenticated_GET(self):
        # check that visiting the route without supplying a param redirects to the locations page and displays a message
        response = self.client.get(reverse('correct_location'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'dropoff_locations/correct_location.html')
        # check that visiting the route with a valid param returns the correct_location template
        response = self.client.get(reverse('correct_location'), {'id': 2})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/correct_location.html')
        # check that visiting a route where the current user has site manager permission returns an update_location template
        ManagerSitePermission.objects.create(site=self.dropoff, user=self.user)
        response = self.client.get(reverse('correct_location'), {'id': 2})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(response.url, reverse('update_location')+'?id=2')
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertTemplateUsed(response, 'dropoff_locations/update_location.html')

    def test_correct_location_POST(self):
        # check that posting to correct_location with no data returns a warning message
        response = self.client.post(reverse('correct_location'), data={})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('locations'))
        # check that posting to correct_location with valid data returns a thanks template
        response = self.client.post(reverse('correct_location'), data={
            'id': 1,
            'first_name': 'tal',
            'last_name': 'zaken',
            'location_name': 'test',
            'location_address': 'test',
            'location_description': 'test',
            'neighborhood_name': 'test',
            'city': 'test',
            'phone': '1-(123)-456.7890',
            'website': 'www.test.com',
            'longitude': -71,
            'latitude': 43,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dropoff_locations/thanks.html')




