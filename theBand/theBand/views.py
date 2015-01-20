from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def discog(request):
	return render(request, 'discog.html', {})

def tourdates(request):
	return render(request, 'tourdates.html', {})
