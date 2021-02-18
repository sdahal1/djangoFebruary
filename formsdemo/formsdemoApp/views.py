from django.shortcuts import render, HttpResponse, redirect

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
    request.session['forminfo'] = request.POST

    print("**********")
    

    return redirect("/orderdetails")

def details(request):
    return render(request, "orderdetails.html")




#{'forminfo': <QueryDict: {'csrfmiddlewaretoken': ['x9zW3GN9GS3EnnrMcc4WR47JmLwGs0NQGPXLlrwqHohdmZIsZKnA7rot2LK7N4LC'], 'fname': ['Saurabh'], 'lname': ['Dahal'], 'email': ['sdahal@codingdojo.com'], 'ccn': ['897y876876'], 'plan': ['16.99']}> }

