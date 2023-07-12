import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
django.setup()



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from users.models import CustomUser

class AddUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = '__all__'


if __name__ == '__main__':
    queryset = CustomUser.objects
    print("-"*30)
    print("Object no filter type")
    print("-"*30)
    print(type(queryset))
    print("-"*30)
    print("Object no filter palain queryset")
    print("-"*30)
    print(queryset)
    queryset = CustomUser.objects.all()
    print("-"*30)
    print("plain queryset type using all filter")
    print("-"*30)
    print(type(queryset))
    print("-"*30)
    print("plain queryset using all filter")
    print("-"*30)
    print(queryset)
    print("-"*30)
    print("plain queryset first resultset item")
    print("-"*30)
    print(queryset[0])
    print("-"*30)
    print("plain queryset first resultset item type")
    print("-"*30)
    print(type(queryset[0]))
    print("-"*30)
    print("plain queryset first resultset class object id")
    print("-"*30)
    print(queryset[0].id)
    print("-"*30)
    print("plain queryset first resultset class all fields")
    print("-"*30)
    print(queryset[0]._meta.fields)

