from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return redirect('home')
def home(request):
    return render(request, 'bbq/bbqhome.html')

def bbq_rent(request):
    return render(request, 'bbq/bbqrent.html')


def admin(request):
    if request.user.is_superuser:
        return render(request, 'admin/admin.html')
    else:
        return redirect('home')