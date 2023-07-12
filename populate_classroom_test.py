import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
django.setup()



#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import get_user_model
from users.models import classroom



if __name__ == '__main__':
            classroom.objects.create(roomtype='lab',capacity=-10,location='Tower',room_number='TWR-211',campus='Newbuurg')
