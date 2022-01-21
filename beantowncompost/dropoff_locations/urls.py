from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('vote/', views.vote),
    path('add_location/', views.add_location),
    path('correct_location/', views.correct_location),
]