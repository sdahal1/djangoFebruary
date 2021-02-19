from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("createTeam", views.createTeam),
    path("createPlayer", views.createPlayer)
]