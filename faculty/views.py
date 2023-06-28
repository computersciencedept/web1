from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    """ main landing page for or website """
    return render(request,"csc108/mainlandingpage.html")
@login_required
def home(request):
    return render(request,"faculty/home.html")





# Create your views here.
