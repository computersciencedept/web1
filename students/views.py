from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    return render(request,"students/home.html")


# Create your views here.
