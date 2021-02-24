from django.shortcuts import render, redirect
from django.contrib import messages
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

    User.objects.create(firstName = request.POST['fname'], lastName= request.POST['lname'] , email = request.POST['email'] , password = request.POST['pw'] , birthday = request.POST['birthday'])


    return redirect("/")