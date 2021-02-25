from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    print(request.POST)
    errorsFromValidator = User.objects.registrationValidator(request.POST)
    print("********", errorsFromValidator)
    if len(errorsFromValidator) > 0:
        for key, value in errorsFromValidator.items():
            messages.error(request, value)
        return redirect("/")

    encryptedPw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()

    newuser = User.objects.create(firstName = request.POST['fname'], lastName= request.POST['lname'] , email = request.POST['email'] , password = encryptedPw , birthday = request.POST['birthday'])

    request.session['loggedInUserId']= newuser.id


    return redirect("/newsFeed")

def newsFeed(request):
    if 'loggedInUserId' not in request.session:
        messages.error(request, "You must be logged in to view the news feed")
        return redirect("/")

    context = {
        'loggedinUser': User.objects.get(id= request.session['loggedInUserId'])
    }

    return render(request, "newsfeed.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")

def login(request):
    print(request.POST)
    errorsFromValidator= User.objects.loginValidator(request.POST)
    print("********PRINTING THE LOGIN ERRORS",errorsFromValidator)
    if len(errorsFromValidator)>0:
        for key, value in errorsFromValidator.items():
            messages.error(request, value)
        return redirect("/")
    
    matchingemail = User.objects.filter(email = request.POST['email'] )
    request.session['loggedInUserId']= matchingemail[0].id

    return redirect("/newsFeed")