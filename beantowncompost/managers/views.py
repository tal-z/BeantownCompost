from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from dropoff_locations.views import get_map
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
    sites = request.user.managerprofile.sites
    map = get_map(sites)
    map_html = map._repr_html_()
    map_id = map.get_name()

    return render(request, 'managers/profile.html', {'sites': sites, 'map': map_html, 'map_id': map_id})