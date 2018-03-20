from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required

def index(request):
	return render(request, 'accounts/index.html')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db
			user.profile.access = form.cleaned_data.get('access')
			user.save()
			return render(request, 'accounts/login.html')

	else:
		form = RegistrationForm()

	args = {'form' : form}
	return render(request, 'accounts/reg_form.html', args)

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return render(request, 'accounts/index.html')

			else:
				return HttpResponse("Invalid login essentials", {})
	else:
		form = LoginForm()

	return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')