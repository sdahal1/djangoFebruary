from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    print("********")
    # Team.objects.all() - gets all the records in the table
    print(Team.objects.all())
    print("********")
    context = {
        'allteams':Team.objects.all()
    }
    return render(request, "index.html", context)


def createTeam(request):
    print("PRINTING FORM DATA")
    print(request.POST)
    print("PRINTING FORM DATA")
    Team.objects.create(name = request.POST['teamname'], location=request.POST['loc'])
    return redirect("/")

def createPlayer(request):
    print("PRINTING FORM DATA")
    print(request.POST)
    print("PRINTING FORM DATA")
    Player.objects.create(firstname = request.POST['fname'], lastname = request.POST['lname'], pointsPerGame= request.POST['ppg'], assignedTeam= Team.objects.get(id=request.POST['team']))
    return redirect("/")