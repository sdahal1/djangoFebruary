from django.shortcuts import render, HttpResponse, redirect

from .models import * 

# Create your views here.
def index(request):

    context = {
        'allshows': TvShow.objects.all() #<QuerySet [<TvShow: TvShow object (1)>, <TvShow: TvShow object (3)>, <TvShow: TvShow object (4)>]>
    }

    return render(request, "shows.html", context)

def createShow(request):
    #a function handling a post request must REDIRECT!
    print("SUBMITTED THE FORM! IN THE CREATE SHOW FUNCTION THEN REDIRECTING ")
    #request.POST represents the information collected from the form
    print("*********")
    print(request.POST)
    print(request.POST['title'])
    print(request.POST['rd'])
    TvShow.objects.create(title=request.POST['title'], description=request.POST['desc'], release_date=request.POST['rd'], rating = request.POST['rating'])
    print("*********")
    return redirect('/')