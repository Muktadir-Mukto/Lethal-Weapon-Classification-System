from  django import forms
from .models import addpost

class postform(forms.ModelForm):
    class Meta:
         model = addpost
         fields = '__all__'
         widgets = {
             'Post' : forms.Textarea(attrs={'class': 'form-control'}),
             'author': forms.Select(attrs={'class': 'form-control'}),

         }