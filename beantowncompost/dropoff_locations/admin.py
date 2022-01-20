from django.contrib.gis import admin
from .models import DropoffLocation

@admin.register(DropoffLocation)
class MyAdmin(admin.GeoModelAdmin):
    pass
