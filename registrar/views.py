from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .forms import AddUserForm
from django.contrib import messages
from users.models import CustomUser

def index(request):
    """ main landing page for or website """
    return render(request,"registrar/home.html")
@login_required
def home(request):
    if(request.session['role'] != 'admin'):
        return HttpResponse('401 Unauthorized', status=401)
        return render(request, '404.html', status=404)
    else:
        return render(request,"registrar/home.html")

@login_required
def adduser(request):
    flag = 0
    if(request.session['role'] != 'admin'):
        return HttpResponse('401 Unauthorized', status=401)
    else:
        if request.POST:  #submitting a completed form   
           flag = 1
           form = AddUserForm(request.POST)

           if form.is_valid():

               temp_form = form.save(commit=False)
               temp_form.set_password("temp123!123!")

               temp_form.save()
               return redirect('registrar')
           else:
               for error in list(form.errors.values()):
                 messages.error(request, error)
               
        #not a post but a get. getting the form for first time
        #or something failed in the is_valid() or save
        context = {}
        context['inadduser'] = 1
        if(flag == 1):
            context['form'] = form
        else:
            context['form'] = AddUserForm()


        return render(request,"registrar/adduser.html",context)

@login_required
def emptypage(request):
    return render(request,"registrar/emptypage.html")
@login_required
def allusers(request):
    if(request.session['role'] != 'admin'):
        return HttpResponse('401 Unauthorized', status=401)
    else:
       queryset = CustomUser.objects.all()
       context={}
       context['query'] = queryset
       context['inallusers'] = 1
       return render(request, 'registrar/allusers.html', context)


