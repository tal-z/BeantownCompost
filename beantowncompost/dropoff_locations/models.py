from tkinter import CASCADE
from django.contrib.gis.db import models
from django.contrib.auth.models import Group
from django.contrib.gis.geos import Point

# Create your models here.
class DropoffLocation(models.Model):
    # Regular Django fields corresponding to the attributes in dropoff_locations.csv
    neighborhood_name = models.CharField(max_length=100, null=True, blank=False)
    location_name = models.CharField(max_length=100, null=True)
    location_description = models.CharField(max_length=1000, null=True, blank=False)
    location_address = models.CharField(max_length=1000, null=True, blank=False)
    phone = models.CharField(max_length=500, null=True, blank=False)
    url = models.CharField(max_length=500, null=True, blank=False, name='website')
    x = models.FloatField(default=None, null=True, blank=False, name='longitude')
    y = models.FloatField(default=None, null=True, blank=False, name='latitude')
    point = models.PointField(srid=4326, default=None, null=True, blank=True)
    city = models.CharField(max_length=100, default=None, null=True, blank=False)


    # Returns the string representation of the model.
    def __str__(self):
        return self.location_name + ' Dropoff'
    

class SuggestDropoffLocation(models.Model):
    # Regular Django fields corresponding to the attributes in dropoff_locations.csv
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    neighborhood_name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    location_description = models.CharField(max_length=1000)
    location_address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=500)
    url = models.CharField(max_length=500, name='website')
    x = models.FloatField(default=None, null=True, name='longitude')
    y = models.FloatField(default=None, null=True, name='latitude')
    # GeoDjango-specific: a geometry field (PointField)
    point = models.PointField(srid=4326, default=None, null=True, blank=True)
    city = models.CharField(max_length=100, default=None, null=True)
    status = models.CharField(max_length=100, default="Awaiting Review", name='status')

    # Returns the string representation of the model.
    def __str__(self):
        return self.location_name + ' New Dropoff Suggestion'


class CorrectDropoffLocation(models.Model):
    # Regular Django fields corresponding to the attributes in dropoff_locations.csv
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    neighborhood_name = models.CharField(max_length=100, blank=True)
    location_name = models.CharField(max_length=100, blank=True)
    location_description = models.CharField(max_length=1000, blank=True)
    location_address = models.CharField(max_length=1000, blank=True)
    phone = models.CharField(max_length=500, blank=True)
    url = models.CharField(max_length=500, blank=True, name='website')
    x = models.FloatField(default=None, null=True, blank=True, name='longitude')
    y = models.FloatField(default=None, null=True, blank=True, name='latitude')
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    point = models.PointField(srid=4326, default=None, null=True, blank=True)
    city = models.CharField(max_length=100, default=None, null=True, blank=True)
    status = models.CharField(max_length=100, default="Awaiting Review", name='status')

    # Returns the string representation of the model.
    def __str__(self):
        return self.location_name + ' Dropoff Correction'


class VoteDropoffLocation(models.Model):
    # Regular Django fields corresponding to the attributes in dropoff_locations.csv
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    zip = models.CharField(max_length=1000)
    x = models.FloatField(default=None, null=True, name='longitude')
    y = models.FloatField(default=None, null=True, name='latitude')
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    point = models.PointField(srid=4326, default=None, null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.first_name + " " + self.last_name