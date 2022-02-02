from django.shortcuts import render, redirect
import folium
from folium import plugins

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import DropoffLocation
from .forms import DropoffLocationForm, AddDropoffLocationForm, CorrectDropoffLocationForm, VoteDropoffLocationForm
from django.contrib import messages


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
    map = get_map([dropoff], start_coords=(dropoff.latitude-.05, dropoff.longitude))
    map_html = map._repr_html_()
    map_id = map.get_name()
    form = DropoffLocationForm(instance=dropoff)
    return render(request, 'dropoff_locations/correct_location.html', {'map': map_html, 'map_id': map_id, 'form': form, 'dropoff': dropoff})

def locations(request):
    locations = DropoffLocation.objects.all().order_by('pk')
    map = get_map(locations)
    map_html = map._repr_html_()
    map_id = map.get_name()
    return render(request, 'dropoff_locations/locations.html', {'map': map_html, 'map_id': map_id, 'locations': locations})

