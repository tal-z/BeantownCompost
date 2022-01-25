from django.db import models
from django.contrib.auth.models import User
from dropoff_locations.models import DropoffLocation
class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #sites = models.CharField(max_length=100)
    site1 = models.ForeignKey(DropoffLocation, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='site_1')
    site2 = models.ForeignKey(DropoffLocation, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='site_2')
    site3 = models.ForeignKey(DropoffLocation, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='site_3')

    def __str__(self):
        return f"{self.user.username} Manager Profile"
