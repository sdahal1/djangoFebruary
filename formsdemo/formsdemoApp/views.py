from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print("**********")
    print(request.method)
    print("**********")

    return render(request, "index.html")

def registerUser(request):
    print("**********")
    #THE INFORMATION COLLECTED FROM THE FORM IS AVAILABLE and represented by THE KEYWORD REQUEST.POST
    print(request.POST)
    print("**********")
    context = {
        'forminfo': request.POST
    }

    return render(request, "orderdetails.html", context)