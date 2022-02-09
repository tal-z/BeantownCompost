from django.db import models
from django.contrib.auth.models import User
from dropoff_locations.models import DropoffLocation



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
    notes = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        unique_together= (('user', 'site'),)
    
    def __str__(self):
        return f'{self.user} {self.site} management permission'
