from django.contrib.gis.db import models

# Create your models here.
class DropoffLocation(models.Model):
    # Regular Django fields corresponding to the attributes in dropoff_locations.csv
    neighborhood_name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    location_description = models.CharField(max_length=1000)
    location_address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    x = models.FloatField()
    y = models.FloatField()
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    point = models.PointField()
    city = models.CharField(max_length=100, default=None)


    # Returns the string representation of the model.
    def __str__(self):
        return self.name