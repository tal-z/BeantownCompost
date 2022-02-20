import folium
from folium import plugins

# Create your views here.
from django.shortcuts import render, redirect
from .models import DropoffLocation, SuggestDropoffLocation, CorrectDropoffLocation
from .forms import DropoffLocationForm, SuggestDropoffLocationForm, CorrectDropoffLocationForm, VoteDropoffLocationForm, ReviewSuggestDropoffForm, UpdateDropoffLocationForm
from managers.models import ManagerSitePermission
from managers.forms import GrantManagerPermissionForm, RequestManagerPermissionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


def get_map(locations, height='100%', start_coords=(42.36034, -71.0578633)):
    folium_map = folium.Map(location=start_coords, tiles='OpenStreetMap', height=height)
    plugins.LocateControl(keepCurrentZoomLevel=True).add_to(folium_map)
    dropoff_points = []
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
        dropoff_points.append([dropoff.latitude, dropoff.longitude])
    if dropoff_points:
        sw_bound = min(item[0] for item in dropoff_points), min(item[1] for item in dropoff_points)
        ne_bound = max(item[0] for item in dropoff_points), max(item[1] for item in dropoff_points)
        folium_map.fit_bounds([sw_bound, ne_bound])

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
            return render(request, 'dropoff_locations/thanks.html', {'action': 'voting for a new drop-off'})
    locations = DropoffLocation.objects.all()
    map = get_map(locations)    
    map_html = map._repr_html_()
    map_id = map.get_name()
    form = VoteDropoffLocationForm()
    return render(request, 'dropoff_locations/vote.html', {'map': map_html, 'map_id': map_id, 'form': form})

def locations(request):
    locations = DropoffLocation.objects.all().order_by('location_name')
    map = get_map(locations)
    map_html = map._repr_html_()
    map_id = map.get_name()
    return render(request, 'dropoff_locations/locations.html', {'map': map_html, 'map_id': map_id, 'locations': locations})


def suggest_location(request):
    if request.method == 'POST':
        form = SuggestDropoffLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dropoff_locations/thanks.html', {'action': 'suggesting a new location'})
    locations = DropoffLocation.objects.all()
    map = get_map(locations)
    map_html = map._repr_html_()
    map_id = map.get_name()
    form = SuggestDropoffLocationForm()
    return render(request, 'dropoff_locations/suggest_location.html', {'map': map_html, 'map_id': map_id, 'form': form})


def correct_location(request):
    if request.method == 'POST':
        form = CorrectDropoffLocationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return render(request, 'dropoff_locations/thanks.html', {'action': 'submitting your correction'})
        messages.warning(request, "Uh oh! There was a problem with your form submission. Check the fields and try again!")
    dropoff = DropoffLocation.objects.get(pk=request.GET.get('id', None))
    if request.user.is_authenticated:
        id = int(request.GET.get('id'))
        site_permissions = ManagerSitePermission.objects.filter(user=request.user)
        if id in {perm.site.id for perm in site_permissions}:
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
            id = int(request.POST.get('id'))
            site_permissions = ManagerSitePermission.objects.filter(user=request.user)
            print(site_permissions)
            if id in {perm.site.id for perm in site_permissions}:
                dropoff = DropoffLocation.objects.get(id=id)                
                form = UpdateDropoffLocationForm(request.POST, instance=dropoff)
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
    form = UpdateDropoffLocationForm(instance=dropoff)
    return render(request, 'dropoff_locations/update_location.html', {'map': map_html, 'map_id': map_id, 'form': form, 'dropoff': dropoff})






@login_required
def request_management_permission(request):
    if request.method == 'POST':
        dropoff=DropoffLocation.objects.get(id=request.POST.get('site'))
        perm = ManagerSitePermission(site=dropoff, user=request.user)
        perm.save()
        return render(request, 'dropoff_locations/thanks.html', {'action': 'requesting management permission'})
    form = RequestManagerPermissionForm()
    return render(request, 'dropoff_locations/request_management_permission.html', {'form': form})


@login_required
@permission_required('managers.change_managerprofile', raise_exception=True)
def update_site_managers(request):
    permissions = ManagerSitePermission.objects.all().order_by('site')
    if request.method == 'POST':
        for permission in permissions:
            status = request.POST.get(f'{permission.site.__str__().replace(" ", "_")}-{permission.user}-status')
            if status and status != permission.status:
                permission.status = status
                permission.save()
                messages.success(request, f"You've set {permission.user}'s permission to edit {permission.site} as '{permission.status}'!")
    per_forms = [(per, GrantManagerPermissionForm(instance=per, prefix=f'{per.site.__str__().replace(" ","_")}-{per.user}'), per.site.__str__().replace(" ","_")) for per in permissions]
    return render(request, 'dropoff_locations/ProjectManager/update_site_managers.html', {'per_forms': per_forms})


@login_required
@permission_required('dropoff_locations.add_dropofflocation', raise_exception=True)
def add_location(request):
    if request.method == 'POST':
        form = DropoffLocationForm(request.POST)
        form.fields['id'].required = False
        if form.is_valid():
            form.save()
            return render(request, 'dropoff_locations/thanks.html', {'action': 'adding a drop-off location'})
        messages.warning(request, "Uh oh! There was a problem with your form submission. Check the fields and try again!")
    locations = DropoffLocation.objects.all().order_by('pk')
    map = get_map(locations)
    map_html = map._repr_html_()
    map_id = map.get_name()
    form = DropoffLocationForm()
    return render(request, 'dropoff_locations/ProjectManager/add_location.html', {'map': map_html, 'map_id': map_id, 'locations': locations, 'form': form})


@login_required
@permission_required('dropoff_locations.add_dropofflocation', raise_exception=True)
def review_suggested_locations(request):
    if request.method == 'POST':
        if 'add-site' in request.POST:
            #add site to map and mark suggestion as resolved.
            form = DropoffLocationForm(request.POST)
            suggestion = SuggestDropoffLocation.objects.get(id=request.POST.get('id'))
            suggestion.status = 'Added to Map'
            suggestion.save(force_update=True)
            if form.is_valid():
                form.save()
                return render(request, 'dropoff_locations/thanks.html', {'action': 'adding a drop-off location'})
        elif 'remove-from-queue' in request.POST:
            # remove from queue by denying site
            suggestion = SuggestDropoffLocation.objects.get(id=request.POST.get('id'))
            suggestion.status = 'Denied'
            suggestion.save(force_update=True)
            return render(request, 'dropoff_locations/thanks.html', {'action': 'reviewing this drop-off location'})
        elif 'id' in request.POST:
            suggestion = SuggestDropoffLocation.objects.get(id=request.POST.get('id'))
            data = {'id': suggestion.id}
            for field in suggestion._meta.fields:
                if field.name in DropoffLocationForm.Meta.fields:
                    val = getattr(suggestion, field.name)
                    data[field.name] = val
            form = ReviewSuggestDropoffForm(data)
            map = get_map([suggestion], start_coords=(suggestion.latitude, suggestion.longitude))
            map_html = map._repr_html_()
            map_id = map.get_name()
            return render(request, 'dropoff_locations/ProjectManager/review_location.html',  {'map': map_html, 'map_id': map_id, 'locations': [suggestion], 'form': form})
        messages.warning(request, "Something went wrong with your request to review a location. Please try again or contract the administrator.")
    suggestions = SuggestDropoffLocation.objects.filter(status='Awaiting Review').order_by('location_name')
    return render(request, 'dropoff_locations/ProjectManager/review_suggested_locations.html', {'suggestions': suggestions})



@login_required
@permission_required('dropoff_locations.change_dropofflocation', raise_exception=True)
def review_suggested_corrections(request):
    corrections = CorrectDropoffLocation.objects.filter(status='Awaiting Review').order_by('location_name')
    return render(request, 'dropoff_locations/ProjectManager/review_suggested_corrections.html', {'corrections': corrections})

