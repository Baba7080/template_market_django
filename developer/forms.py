from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import TextInput
from time import time
import datetime
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from datetime import time
class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))
    date_of_join = forms.DateField(initial=datetime.date.today)
    # time_join = forms.DateTimeField(initial=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time_of_join = forms.TimeField(initial=datetime.datetime.now)
    #  forms.DateTimeField(initial = datetime.datetime.now)
    # Category = forms.ChoiceField(choices = Catogories)
    class Meta:
        model = User
        fields = ['username','date_of_join','time_of_join','email','password1','password2']
        label = {'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
        {'autocomplete':'current-password', 'class':'form-control'}))
