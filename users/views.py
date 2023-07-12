#from django.shortcuts import render
#from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(None, data=request.POST)
        if form.is_valid():

            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.username}! You have been logged in")
                queryset = CustomUser.objects.filter(username=form.cleaned_data['username']).values('status')
                user_type = queryset[0]['status']
                request.session['role'] = user_type
                #print(user_type)
                if(user_type == 'faculty'):
                     
                     return redirect('faculty')
                elif(user_type == 'admin'):
                    return redirect('registrar')
                elif(user_type == 'student'):
                    return redirect('students')

                else:
                     return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm() 
    
    return render(
        request=request,
        template_name="users/login.html", 
        context={'form': form}
        )


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")
# Create your views here.

