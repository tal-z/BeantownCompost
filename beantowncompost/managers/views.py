import site
from django.forms import forms
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from markupsafe import re
from dropoff_locations.views import index
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)   
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your account has been created! Now go ahead and log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'managers/register.html', {'form': form})


@login_required
def profile(request):
    sites = [request.user.managerprofile.site1, request.user.managerprofile.site2, request.user.managerprofile.site3]
    print(sites)
    sites = [site for site in sites if site != None]
    return render(request, 'managers/profile.html', {'sites': sites})