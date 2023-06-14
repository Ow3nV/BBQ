from django.contrib import messages
from django.db.models.functions import Lower
from django.http import HttpResponse
from django.shortcuts import render, redirect

from bbqweb.forms import BarbequeForm
from bbqweb.models import Barbeque, Images


# Create your views here.
def index(request):
    return redirect('home')
def home(request):
    return render(request, 'bbq/bbqhome.html')

def bbq_rent(request):
    bbqs = Barbeque.objects.all()

    return render(request, "bbq/bbqrent.html", {'bbqs': bbqs})


def bbq_rent_day(request):
    bbqs = Barbeque.objects.all().order_by('rent_day')
    return render(request, "bbq/bbqrent.html", {'bbqs': bbqs})

def bbq_rent_day_high(request):
    bbqs = Barbeque.objects.all().order_by('-rent_day')
    return render(request, "bbq/bbqrent.html", {'bbqs': bbqs})

def bbq_rent_name(request):
    bbqs = Barbeque.objects.all().order_by(Lower('name'))
    return render(request, "bbq/bbqrent.html", {'bbqs': bbqs})






def view_bbq(request, barbeque_id):
    image_list = []
    bbq = Barbeque.objects.get(id=barbeque_id)
    imgs = Images.objects.get(barbeque=bbq)
    if imgs.image1:
        image_list.append(imgs.image1.url)
    if imgs.image2:
        image_list.append(imgs.image2.url)
    if imgs.image3:
        image_list.append(imgs.image3.url)
    if imgs.image4:
        image_list.append(imgs.image4.url)

    return render(request, "bbq/viewbbqrent.html", {'bbq': bbq, 'imgs': image_list})
