from http import client
from django.test import TestCase, Client
from django.urls import reverse
from managers.models import ManagerSitePermission
from django.contrib.auth.models import User

class TestViews(TestCase):
    
    def setUp(self):
        user = User.objects.create(username='test_ProjectManager')
        user.set_password('SayCompost')
        user.save()
        self.client = Client()
        self.client.login(username="test_ProjectManager", password="SayCompost")
        self.register_url = reverse('register')
        self.my_sites_url = reverse('my_sites')
        self.my_account_url = reverse('my_account')

    def test_managers_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'managers/auth/register.html')

    
    def test_managers_register_POST(self):
        response = self.client.post(self.register_url, {
            'email': 'talzaken+unittest@gmail.com',
            'username': 'test_newuser1',
            'password1': 'SayCompost1',
            'password2': 'SayCompost1',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.headers['Location'], '/login/')


    def test_managers_my_sites_unauthenticated_GET(self):
        self.client.logout()
        response = self.client.get(self.my_sites_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.headers['Location'], '/login/?next=/my_sites/')


    def test_managers_my_sites_authenticated_GET(self):
        response = self.client.get(self.my_sites_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'managers/my_sites.html')


    def test_managers_my_account_unauthenticated_GET(self):
        self.client.logout()
        response = self.client.get(self.my_account_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.headers['Location'], '/login/?next=/my_account/')


    def test_managers_my_account_authenticated_GET(self):
        response = self.client.get(self.my_account_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'managers/my_account.html')


