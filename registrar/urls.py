from django.urls import path

from . import views

urlpatterns = [
    path("registrar/", views.home, name="registrar"),
    path("registrar/adduser/", views.adduser, name="adduser"),
    path("registrar/allusers/",views.allusers,name="allusers"),
    path("emptypage",views.emptypage,name="emptypage")
]

