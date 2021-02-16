from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def home(request):
    return redirect("/teams") #this is the response 


def showTeams(request):
    return HttpResponse("Great job team, this is where we will later show all teams in an html page")

def new(request):
    return HttpResponse("placeholder to show a form to create a new team")


def showSpecificTeam(request, teamname):
    return HttpResponse(f"showing info about specific team: {teamname}")