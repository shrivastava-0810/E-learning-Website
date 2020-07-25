from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def register(request):
	if request.method == 'POST':
		#user has info and wants an account 
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(email=request.POST['email'])
				return(render(request, 'accounts/register.html', {'error':'E-mail already exists'}))
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['email'], first_name=request.POST['first_name'],
				last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password1'])
				auth.login(request, user)
				return(redirect('home'))
		else:
			return(render(request, 'accounts/register.html', {'error':'Passwords must be same'}))
	else:
		#user wants to enter info
		return(render(request, 'accounts/register.html'))

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return(redirect('home'))
		else:
			return(render(request, 'accounts/login.html', {'error':'E-mail or password is incorrect'}))	
	else:
		return(render(request, 'accounts/login.html'))

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return(redirect('home'))