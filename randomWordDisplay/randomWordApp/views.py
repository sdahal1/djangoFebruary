from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    topratedMovies = [
        {
            "title": "Top Gun",
            "rating": 5,
            "release_date": "2000-03-01"
        },
        {
            "title": "Fight Club",
            "rating": 5,
            "release_date": "1999-05-08"
        },
        {
            "title": "Step Brothers",
            "rating": 5,
            "release_date": "2010-01-01"
        },
        {
            "title": "Shutter Island",
            "rating": 5,
            "release_date": "2008-03-15"
        },
        {
            "title": "Django Unchained",
            "rating": 5,
            "release_date": "2012-12-01"
        },
        {
            "title": "Finding Nemo",
            "rating": 4,
            "release_date": "2012-12-01"
        },
        {
            "title": "Super Mario",
            "rating": 2,
            "release_date": "2012-12-01"
        }
    ]
    #in order to pass information from the server (views.py) to the html, I need a context dictionary with the info I want to pass
    favorite_color = "blue"

    context = {
        "topmovs": topratedMovies,
        'favcolor': favorite_color,
        'random': random.randint(0,99)
    }
    # print("************")
    # print(random.randint(0,99))
    # print("************")

    return render(request, "randomword.html", context)
