from django.urls import path
from . import views

urlpatterns = [
    path("menu/new", views.index ),
    path("menu/create", views.createMenuItem),
    path("menu", views.showMenu),
    path("menuItem/info/<int:menuId>", views.menuItemInfo),
    path("menu/delete/<int:menuId>", views.deleteItem),
    path("menu/edit/<int:menuId>", views.editItem),
    path("menu/update/<int:menuId>", views.updateItem)
]