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
from managers.forms import LoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', manager_views.register, name='register'),
    path('profile/', manager_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='managers/login.html',
            authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='managers/logout.html'), name='logout'),
    path('', include('dropoff_locations.urls')),
    path('dropoff/', include('dropoff_locations.urls')),
]
