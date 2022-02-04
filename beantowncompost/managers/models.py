from django.db import models
from django.contrib.auth.models import User
from dropoff_locations.models import DropoffLocation


class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    site1 = models.ForeignKey(DropoffLocation, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='site_1')
    site2 = models.ForeignKey(DropoffLocation, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='site_2')
    site3 = models.ForeignKey(DropoffLocation, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='site_3')


    @property
    def sites(self):
        sites = [self.site1, self.site2, self.site3]
        return [site for site in sites if site != None]


    def __str__(self):
        return f"{self.user.username} Manager Profile"

SITEMANAGER_STATUSES = [
    ('requested', 'requested'),
    ('active', 'active'),
    ('denied', 'denied'),
    ('cancelled', 'cancelled'),
]

class ManagerSitePermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(DropoffLocation, on_delete=models.CASCADE, default=None, null=True)
    status = models.CharField(max_length=50, choices=SITEMANAGER_STATUSES, default='requested')

    class Meta:
        unique_together= (('user', 'site'),)
    
    def __str__(self):
        return f'{self.user} {self.site} management permission'
