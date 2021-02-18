from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    if 'visitcount' in request.session:
        request.session['visitcount'] += 1
    else:
        request.session['visitcount'] = 1
    return render(request, "index.html")


def resetInfo(request):
    #delete the information stored in session
    del request.session['visitcount']
    return redirect("/")
# {'visitcount': 2}