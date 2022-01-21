from django.contrib.gis import admin
from .models import DropoffLocation, AddDropoffLocation, CorrectDropoffLocation, VoteDropoffLocation

admin.site.register(DropoffLocation, admin.GeoModelAdmin)
admin.site.register(AddDropoffLocation, admin.GeoModelAdmin)
admin.site.register(CorrectDropoffLocation, admin.GeoModelAdmin)
admin.site.register(VoteDropoffLocation, admin.GeoModelAdmin)

