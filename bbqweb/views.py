from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django.http import HttpResponse
from django.shortcuts import render, redirect

from bbqweb.forms import BarbequeForm
from bbqweb.models import Barbeque, Images
from order.forms import OrderForm


# Create your views here.
def index(request):
    return redirect('home')


def home(request):
    return render(request, 'bbq/bbqhome.html')


def bbq_rent(request):
    sort_option = request.GET.get('sort')

    if sort_option == 'high':
        queryset = Barbeque.objects.order_by('-rent')
    elif sort_option == 'low':
        queryset = Barbeque.objects.order_by('rent')
    elif sort_option == 'name':
        queryset = Barbeque.objects.order_by('name')
    else:
        queryset = Barbeque.objects.all()
    return render(request, "bbq/bbqrent.html", {'bbqs': queryset})


def bbq_rent_day(request):
    bbqs = Barbeque.objects.all().order_by('rent')
    return render(request, "bbq/bbqrent.html", {'bbqs': bbqs})


def bbq_rent_day_high(request):
    bbqs = Barbeque.objects.all().order_by('-rent')
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