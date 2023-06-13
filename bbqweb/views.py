from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from bbqweb.forms import BarbequeForm
from bbqweb.models import Barbeque


# Create your views here.
def index(request):
    return redirect('home')
def home(request):
    return render(request, 'bbq/bbqhome.html')

def bbq_rent(request):
    bbqs = Barbeque.objects.all()
    return render(request, "bbq/bbqrent.html", {'bbqs': bbqs})



def view_bbq(request, barbeque_id):
    bbq = Barbeque.objects.get(id=barbeque_id)
    return render(request, "bbq/viewbbqrent.html", {'bbq': bbq})
