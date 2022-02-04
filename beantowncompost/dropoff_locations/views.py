import folium
from folium import plugins

# Create your views here.
from django.shortcuts import render, redirect
from .models import DropoffLocation
from .forms import DropoffLocationForm, AddDropoffLocationForm, CorrectDropoffLocationForm, VoteDropoffLocationForm
from managers.models import ManagerSitePermission
from managers.forms import ManagerSitePermissionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


def get_map(locations, height='100%', start_coords=(42.36034, -71.0578633)):
    folium_map = folium.Map(location=start_coords, zoom_start=12, tiles='OpenStreetMap', height=height)
    plugins.LocateControl(keepCurrentZoomLevel=True).add_to(folium_map)
    for dropoff in locations:
        iframe = "<br>".join([f"<b>{dropoff.neighborhood_name}</b>",
                                dropoff.location_name + "<br>",
                                f"<b>Location Instructions:</b>  {dropoff.location_description}",
                                f"<b>Address:</b>  {dropoff.location_address}",
                                f"<b>City:</b>  {dropoff.city}",
                                f"<b>Phone:</b>  {dropoff.phone}<br>",
                                f"<b><a target ='_blank' href='{dropoff.website}'>Visit Website</b></a>",
                                f"<a target ='_parent' href='/correct_location/?id={dropoff.id}'><b>Submit a correction for this bin</b></a>"
                                ])
        popup = folium.Popup(iframe,
                                min_width=250,
                                max_width=500)
        marker = folium.Marker([dropoff.latitude, dropoff.longitude],
                        popup=popup,
                        icon=folium.Icon(color="green", icon="fa-trash", prefix='fa'), marker_id=f'marker_{dropoff.id}'
                        )
        marker.add_to(folium_map)
    return folium_map


def index(request):
    locations = DropoffLocation.objects.all()
    map = get_map(locations)
    map_html = map._repr_html_()
    return render(request, 'dropoff_locations/index.html', {'map': map_html})


def vote(request):
    if request.method == 'POST':
        form = VoteDropoffLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dropoff_locations/thanks.html', {'action': 'voting for a new location'})
    locations = DropoffLocation.objects.all()
    map = get_map(locations)    
    map_html = map._repr_html_()
    map_id = map.get_name()
    form = VoteDropoffLocationForm()
    return render(request, 'dropoff_locations/vote.html', {'map': map_html, 'map_id': map_id, 'form': form})


def add_location(request):
    if request.method == 'POST':
        form = AddDropoffLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dropoff_locations/thanks.html', {'action': 'submitting a new location'})
    locations = DropoffLocation.objects.all()
    map = get_map(locations)
    map_html = map._repr_html_()
    map_id = map.get_name()
    form = AddDropoffLocationForm()
    return render(request, 'dropoff_locations/add_location.html', {'map': map_html, 'map_id': map_id, 'form': form})


def correct_location(request):
    if request.method == 'POST':
        form = CorrectDropoffLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dropoff_locations/thanks.html', {'action': 'submitting your correction'})
    dropoff = DropoffLocation.objects.get(pk=request.GET.get('id', None))
    if request.user.is_authenticated:
            if dropoff.location_name in {site.location_name for site in request.user.managerprofile.sites}:
                messages.info(request, "Hey there! It looks like you're the manager for this site, so you have permission to update the map yourself. This is a heads up that your changes will be made live immediately. If you want to submit a correction for review instead, log out and click the 'Submit a Correction' button.")
                return redirect(f'/update_location/?id={dropoff.id}')
    map = get_map([dropoff], start_coords=(dropoff.latitude, dropoff.longitude))
    map_html = map._repr_html_()
    map_id = map.get_name()
    form = CorrectDropoffLocationForm(instance=dropoff)
    return render(request, 'dropoff_locations/correct_location.html', {'map': map_html, 'map_id': map_id, 'form': form, 'dropoff': dropoff})


@login_required
def update_location(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            loc_name = request.POST.get('location_name')
            if loc_name in {site.location_name for site in request.user.managerprofile.sites}:
                dropoff = DropoffLocation.objects.get(location_name=loc_name)                
                form = DropoffLocationForm(request.POST, instance=dropoff)
                if form.is_valid():
                    form.save()
                    return render(request, 'dropoff_locations/thanks.html', {'action': 'submitting your update'})
        if True:
            messages.info(request, "Heads up! You don't have permission to edit this site. Your submission has been saved, and will be reviewed as a correction.")
            form = CorrectDropoffLocationForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'dropoff_locations/thanks.html', {'action': 'submitting your correction'})
    dropoff = DropoffLocation.objects.get(pk=request.GET.get('id', None))
    map = get_map([dropoff], start_coords=(dropoff.latitude, dropoff.longitude))
    map_html = map._repr_html_()
    map_id = map.get_name()
    form = DropoffLocationForm(instance=dropoff)
    return render(request, 'dropoff_locations/update_location.html', {'map': map_html, 'map_id': map_id, 'form': form, 'dropoff': dropoff})


def locations(request):
    locations = DropoffLocation.objects.all().order_by('pk')
    map = get_map(locations)
    map_html = map._repr_html_()
    map_id = map.get_name()
    return render(request, 'dropoff_locations/locations.html', {'map': map_html, 'map_id': map_id, 'locations': locations})


@login_required
@permission_required('managers.change_managerprofile', raise_exception=True)
def update_site_managers(request):
    permissions = ManagerSitePermission.objects.all().order_by('site')
    if request.method == 'POST':
        print(request.POST)
        print(permissions)
        for permission in permissions:
            status = request.POST.get(f'{permission.site.__str__().replace(" ", "_")}-{permission.user}-status')
            if status and status != permission.status:
                permission.status = status
                permission.save()
                messages.success(request, f"You've set {permission.user}'s permission to edit {permission.site} as '{permission.status}'!")
        #return render(request, 'dropoff_locations/thanks.html', {'action': 'updating site manager permissions'})
    per_forms = [(per, ManagerSitePermissionForm(instance=per, prefix=f'{per.site.__str__().replace(" ","_")}-{per.user}'), per.site.__str__().replace(" ","_")) for per in permissions]
    return render(request, 'dropoff_locations/update_site_managers.html', {'per_forms': per_forms})



@login_required
def request_management_permission(request):
    if request.method == 'POST':
        perm = ManagerSitePermission(site=DropoffLocation.objects.get(location_name=request.POST.get('site')), user=request.user)
        perm.save()
        return render(request, 'dropoff_locations/thanks.html', {'action': 'requesting management permission'})
    dropoffs = DropoffLocation.objects.all()
    return render(request, 'dropoff_locations/request_management_permission.html', {'dropoffs': dropoffs})
