from django.urls import path     
from . import views


urlpatterns = [
    # @app.route("/")
    path('', views.home),
    path("teams", views.showTeams),
    path("teams/new", views.new),
    path("teams/<teamname>", views.showSpecificTeam),
    # path("allfood", views.showAllFoodItems),
    # path("team/<teamname>", views.showSpecificTeam)  
]