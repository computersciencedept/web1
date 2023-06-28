from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 


def index(request):
    """ main landing page for or website """
    return render(request,"csc108/mainlandingpage.html")

def home(request):
    return render(request,"csc108/home.html")


"""
def dictionary_example(request):
    items = {
            "Course Name:": "Web programming 1",
            "Course no:":"csc108",
            "Location:":"Middletown campus",
            }
    context = {"classinfo":items}
    return render(request,"dictionarytemplate.html",context)

def list_example(request):
    mylist = ["Web programming 1","csc108","Middletown campus"]
    return render(request,"listtemplate.html",{"items":mylist})
"""

