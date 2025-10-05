from django import forms
from .models import postBlog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class postForm(forms.ModelForm):
    class Meta:
        model=postBlog
        fields=['text','photo']


class UserRegistrationFrom(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=('username','email','password1','password2')
        
