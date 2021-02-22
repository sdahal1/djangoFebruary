from django.shortcuts import render, HttpResponse, redirect
from .models import *


# Create your views here.
def index(request):
    context = {
        'allArtists': Artist.objects.all()
    }
    return render(request, "index.html", context)

def createArtist(request):
    print(request.POST)
    Artist.objects.create(firstName = request.POST['fname'], lastName=request.POST['lname'], description = request.POST['desc'])

    return redirect("/")

def showArtistInfo(request, artistid):
    context = {
        'oneArtist': Artist.objects.get(id = artistid),
        'allUsers': User.objects.all()

    }
    return render(request, "artistinfo.html", context)


def addToFanBase(request, artistid):
    print(request.POST)
    #need information about the user selected (provided from the dropdown in the form via request.POST)
    this_user = User.objects.get(id=request.POST['selectedUser'])
    print("***************", this_user)
    #need information about the artist that the user is becoming a fan of for the many to many join
    this_artist = Artist.objects.get(id=artistid)

    #make the many to many join (2 options below both do the same thing, one is commented out)
    # this_artist.fans.add(this_user)
    this_user.likedArtists.add(this_artist)



    # User.objects.get(id=3).likedArtists.add(Artist.objects.get(id=5))
    return redirect(f"/showArtistInfo/{artistid}")
