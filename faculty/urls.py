from django.urls import path

from . import views

urlpatterns = [
    path("faculty", views.home, name="faculty"),
]

