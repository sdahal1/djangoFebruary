from django.shortcuts import render, HttpResponse

from .models import * 

# Create your views here.
def index(request):

    context = {
        'allshows': TvShow.objects.all()
    }

    return render(request, "shows.html", context)