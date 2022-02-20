from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_ProjectManager')
        user.set_password('SayCompost')
        user.save()
        self.client = Client()
        self.client.login(username="test_ProjectManager", password="SayCompost")
        

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

