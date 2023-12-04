from django import forms
from .models import Userinfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ('email', 'firstname', 'lastname')