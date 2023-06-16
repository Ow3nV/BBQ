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


def checkout_bbq(request, barbeque_id):
    if request.user.is_authenticated:
        form = OrderForm()
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.barbeque = Barbeque.objects.get(id=barbeque_id)
                order.user = User.objects.get(id=request.user.id)
                days = order.date_to - order.date_from
                if days.days < 7:
                    price = days.days * order.barbeque.rent
                elif 7 < days.days < 28:
                    price = days.days * order.barbeque.rent * 0.65
                else:
                    price = days.days * order.barbeque.rent * 0.5
                if order.delivery:
                    price += order.barbeque.delivery
                if order.pick_up:
                    price += order.barbeque.pickup
                order.sub_total = price
                order.save()
                messages.success(request, "Order Successful")
                return redirect("home")
            messages.error(request, "Unsuccessful Invalid information.")
        return render(request, 'bbq/bbqcheckout.html', {'order_form' : form})
    else:
        messages.warning(request, 'Please Log In')
        return redirect('view_bbq_rent', barbeque_id)
