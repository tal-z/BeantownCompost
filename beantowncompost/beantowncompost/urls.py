"""beantowncompost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from managers import views as manager_views
from managers.forms import LoginForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', manager_views.register, name='register'),
    path('profile/', manager_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='managers/login.html',
            authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='managers/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
            template_name='managers/password_change.html',
            form_class=PasswordChangeForm), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeView.as_view(template_name='managers/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='managers/password_reset_form.html', 
            email_template_name='managers/password_reset_email.html', 
            subject_template_name='managers/password_reset_subject.txt',
            form_class=PasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='managers/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='managers/password_reset_confirm.html',
            form_class=SetPasswordForm), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='managers/password_reset_complete.html'), name='password_reset_complete'),
    path('dropoff/', include('dropoff_locations.urls')),
    path('', include('dropoff_locations.urls')),
]
