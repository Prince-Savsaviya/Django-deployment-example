from django import forms
from django.contrib.auth.models import User
from app1.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta():
        model = User
        fields = ('username', 'email' ,'password')
        #exclude = ('user',)
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pics')
        #exclude = ('user',)