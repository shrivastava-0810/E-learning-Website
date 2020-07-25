from django.shortcuts import render

def home(request):
	return(render(request, 'courses/home.html'))

def courses(request):
	return(render(request, 'courses/courses.html'))