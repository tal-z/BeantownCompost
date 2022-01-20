from django.shortcuts import render
import folium
from folium import plugins

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import DropoffLocation


def index(request):
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
                                  f"<a href='/correct_bin/{dropoff.id}'><b>Submit a correction for this bin</b></a>"
                                  ]
                                 )
            popup = folium.Popup(iframe,
                                 min_width=250,
                                 max_width=500)
            folium.Marker([dropoff.y, dropoff.x],
                          popup=popup,
                          icon=folium.Icon(color="green", icon="fa-trash", prefix='fa'),
                          ).add_to(folium_map)
    map_html = folium_map._repr_html_()



    return render(request, 'dropoff_locations/index.html', {'map': map_html})



def vote(request):
    start_coords = (42.36034, -71.0578633)
    folium_map = folium.Map(location=start_coords, zoom_start=12, tiles='OpenStreetMap', )
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
                                  f"<a href='/correct_bin/{dropoff.id}'><b>Submit a correction for this bin</b></a>"
                                  ]
                                 )
            popup = folium.Popup(iframe,
                                 min_width=250,
                                 max_width=500)
            folium.Marker([dropoff.y, dropoff.x],
                          popup=popup,
                          icon=folium.Icon(color="green", icon="fa-trash", prefix='fa'),
                          ).add_to(folium_map)
    map_html = folium_map._repr_html_()

    map_id = folium_map.get_name()

    return render(request, 'dropoff_locations/vote.html', {'map': map_html, 'map_id': map_id})