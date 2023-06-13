from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bbq/bbqhome.html')

def bbq_rent(request):
    return render(request, 'bbq/bbqrent.html')