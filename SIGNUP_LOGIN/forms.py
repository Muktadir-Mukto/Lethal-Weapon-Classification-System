from django import forms
from .models import Userprofile

class update_user(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields= "__all__"

