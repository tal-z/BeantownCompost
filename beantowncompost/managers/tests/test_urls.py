from django.test import SimpleTestCase, Client, TestCase
from django.urls import reverse, resolve
from managers import views as managers_views 
from managers.forms import LoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

class TestUrls(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_ProjectManager')
        user.set_password('SayCompost')
        user.save()
        self.client = Client()
        #self.client.login(username="test_ProjectManager", password="SayCompost")


    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, managers_views.register)


    def test_my_sites_url_resolves(self):
        url = reverse('my_sites')
        self.assertEquals(resolve(url).func, managers_views.my_sites)

        
    def test_my_account_url_resolves(self):
        url = reverse('my_account')
        self.assertEquals(resolve(url).func, managers_views.my_account)
    
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)
    
    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)
        
    def test_password_change_url_resolves(self):
        url = reverse('password_change')
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordChangeView)
        
    def test_password_change_done_url_resolves(self):
        url = reverse('password_change_done')
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordChangeDoneView)
    
    def test_password_reset_url_resolves(self):
        url = reverse('password_reset')
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetView)
    
    def test_password_reset_done_url_resolves(self):
        url = reverse('password_reset_done')
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetDoneView)
    
    #def test_password_reset_confirm_url_resolves(self):
    #    url = reverse('password_reset_confirm')
    #    self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetConfirmView)
    
    def test_password_reset_complete_url_resolves(self):
        url = reverse('password_reset_complete')
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)
    