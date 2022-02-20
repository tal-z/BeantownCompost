from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
    path('add_location/', views.add_location, name='add_location'),
    path('suggest_location/', views.suggest_location, name='suggest_location'),
    path('correct_location/', views.correct_location, name='correct_location'),
    path('update_location/', views.update_location, name='update_location'),
    path('update_site_managers/', views.update_site_managers, name='update_site_managers'),
    path('request_management_permission/', views.request_management_permission, name='request_management_permission'),
    path('review_suggested_locations/', views.review_suggested_locations, name='review_suggested_locations'),
    path('review_suggested_corrections/', views.review_suggested_corrections, name='review_suggested_corrections'),
    path('locations/', views.locations, name='locations'),
]