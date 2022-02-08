from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import ManagerSitePermission
from dropoff_locations.views import get_map
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)   
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f'An account has been created for {username}! Now go ahead and log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'managers/auth/register.html', {'form': form})


@login_required
def my_sites(request):
    site_permissions = ManagerSitePermission.objects.filter(user=request.user)
    dropoffs = [perm.site for perm in site_permissions]
    map = get_map(dropoffs)
    map_html = map._repr_html_()
    map_id = map.get_name()
    return render(request, 'managers/my_sites.html', {'dropoffs': dropoffs, 'map': map_html, 'map_id': map_id})

@login_required
def my_account(request):
    return render(request, 'managers/my_account.html')