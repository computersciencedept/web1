from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from users.models import CustomUser

class AddUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.HiddenInput(), initial="!&!!!!!123!!!!occc!!!12345")
    password2 = forms.CharField(widget=forms.HiddenInput(), initial="!&!!!!!123!!!!occc!!!12345")
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name","email","status","description"]
        #exclude = ["password1","password2"]
    #def __init__ (self, *args, **kwargs):
    #   super(AddUserForm,self).__init__(*args, **kwargs)
    #   #remove what you like...
    #   self.fields.pop ('password1')
    #   self.fields.pop ('password2')

