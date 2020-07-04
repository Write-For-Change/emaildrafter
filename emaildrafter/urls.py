"""
Defining the url handling for the website as the project's base urls.py points here.
In the future if different Django apps are installed we may wish to move "about-us" (for example) to the main project urls.py, however below best replicates the original Flask setup.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us", views.aboutus, name="aboutus"),
]
