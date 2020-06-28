from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us", views.aboutus, name="aboutus"),
]
