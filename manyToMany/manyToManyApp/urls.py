from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("artist/create", views.createArtist),
    path("showArtistInfo/<int:artistid>", views.showArtistInfo),
    path("addToFanBase/<int:artistid>", views.addToFanBase)
]