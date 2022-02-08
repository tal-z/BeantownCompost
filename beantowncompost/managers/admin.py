from django.contrib import admin
from .models import ManagerSitePermission
# Register your models here.

#admin.site.register(ManagerProfile, admin.ModelAdmin)
admin.site.register(ManagerSitePermission, admin.ModelAdmin)
