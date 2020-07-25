from django.shortcuts import render

def becomeinstructor(request):
	return(render(request, 'becomeinstructor.html'))