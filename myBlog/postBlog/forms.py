from django import forms
from .models import postBlog

class postForm(forms.ModelForm):
    class Meta:
        model=postBlog
        fields=['text','photo']
