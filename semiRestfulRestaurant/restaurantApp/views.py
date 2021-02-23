from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def createMenuItem(request):
    print("***********")
    print(request.POST)
    print("***********")
    newitem = Menu.objects.create(name = request.POST['dishname'], description= request.POST['desc'], price = request.POST['priceInput'])
    print('PRINTING THE NEW ITEM HERE:', newitem)

    return redirect(f"/menuItem/info/{newitem.id}")

def showMenu(request):
    context = {
        'allMenuItems': Menu.objects.all()
    }
    return render(request, "menu.html", context)

def menuItemInfo(request, menuId):
    context = {
        'oneItem': Menu.objects.get(id=menuId)
    }
    return render(request, "menuItemInfo.html", context)

def deleteItem(request, menuId):
    # Deleting an existing record
    menuitem = Menu.objects.get(id=menuId)
    menuitem.delete()
    return redirect("/menu")

def editItem(request, menuId):
    context = {
        'oneItem': Menu.objects.get(id=menuId)
    }
    return render(request, "editmenu.html", context)

def updateItem(request, menuId):
    print("***********")
    print(request.POST)
    print("***********")
    # Updating an existing record
    c = Menu.objects.get(id=menuId)
    c.name = request.POST['dishname']
    c.description = request.POST['desc']
    c.price = request.POST['priceInput']
    c.save()

    return redirect(f"/menuItem/info/{menuId}")