from http.client import HTTPResponse
from django.shortcuts import render, redirect
import folium
from folium import plugins

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import DropoffLocation
from .forms import DropoffLocationForm, AddDropoffLocationForm, CorrectDropoffLocationForm, VoteDropoffLocationForm
from django.forms import HiddenInput
from django.contrib import messages

def get_map():
    start_coords = (42.36034, -71.0578633)
    folium_map = folium.Map(location=start_coords, zoom_start=12, tiles='OpenStreetMap')
    plugins.LocateControl(keepCurrentZoomLevel=True).add_to(folium_map)
    locations = DropoffLocation.objects.all()
    for dropoff in locations:
            iframe = "<br>".join([f"<b>{dropoff.neighborhood_name}</b>",
                                  dropoff.location_name + "<br>",
                                  f"<b>Location Instructions:</b>  {dropoff.location_description}",
                                  f"<b>Address:</b>  {dropoff.location_address}",
                                  f"<b>City:</b>  {dropoff.city}",
                                  f"<b>Phone:</b>  {dropoff.phone}<br>",
                                  f"<b><a target ='_blank' href='{dropoff.url}'>Visit Website</b></a>",
                                  f"<a target ='_parent' href='/correct_location/?id={dropoff.id}'><b>Submit a correction for this bin</b></a>"
                                  ]
                                 )
            popup = folium.Popup(iframe,
                                 min_width=250,
                                 max_width=500)
            folium.Marker([dropoff.y, dropoff.x],
                          popup=popup,
                          icon=folium.Icon(color="green", icon="fa-trash", prefix='fa'),
                          ).add_to(folium_map)
    return folium_map


def index(request):
    map = get_map()
    map_html = map._repr_html_()
    return render(request, 'dropoff_locations/index.html', {'map': map_html})


def vote(request):
    print("voting!")
    if request.method == 'POST':
        form = VoteDropoffLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dropoff_locations/thanks.html', {'action': 'voting for a new location'})
    map = get_map()
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
    form = AddDropoffLocationForm()
    return render(request, 'dropoff_locations/add_location.html', {'form': form})


def correct_location(request):
    if request.method == 'POST':
        form = CorrectDropoffLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dropoff_locations/thanks.html', {'action': 'submitting your correction'})
    location = DropoffLocation.objects.get(pk=request.GET.get('id', None))
    form = DropoffLocationForm(instance=location)
    return render(request, 'dropoff_locations/correct_location.html', {'form': form})

    