from django import forms
from django.forms import ModelForm
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
	ACCESS_OPTIONS = (
		('Admin', 'Admin'),
		('Client', 'Client'),
		('Customer', 'Customer'),
		)

	access = forms.ChoiceField(choices=ACCESS_OPTIONS, required=True)

	class Meta:
		model = User
		fields = {'username', 'password1', 'password2', 'access',}

class LoginForm(forms.Form):
	ACCESS_OPTIONS = (
		('Admin', 'Admin'),
		('Client', 'Client'),
		('Customer', 'Customer'),
		)
	username = forms.CharField(label='username', max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())
