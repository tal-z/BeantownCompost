from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('vote/', views.vote),
    path('add_location/', views.add_location),
    path('correct_location/', views.correct_location),
    path('update_location/', views.update_location),
    path('update_site_managers/', views.update_site_managers, name='update_site_managers'),
    path('request_management_permission/', views.request_management_permission, name='request_management_permission'),
    path('locations/', views.locations),
]