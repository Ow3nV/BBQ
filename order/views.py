from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date

from bbqweb.models import Barbeque
from order.forms import OrderForm, CalenderForm


# Create your views here.

def checkout_bbq(request, barbeque_id):
    if request.user.is_authenticated:
        form = OrderForm()
        date_from = parse_date(request.session['date_from'])
        date_to = parse_date(request.session['date_to'])
        delivery= request.session['delivery']
        pick_up = request.session['pickup']
        bbq = Barbeque.objects.get(id=barbeque_id)
        days = date_to - date_from
        if days.days < 7:
            price = days.days * bbq.rent
            if days.days == 0:
                price = 1 * bbq.rent
        elif 7 < days.days < 28:
            price = days.days * bbq.rent * 0.65
        else:
            price = days.days * bbq.rent * 0.5
        if delivery:
            price += bbq.delivery
        if pick_up:
            price += bbq.pickup
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.barbeque = bbq
                order.user = User.objects.get(id=request.user.id)
                order.delivery = delivery
                order.pick_up = pick_up
                order.date_from = date_from
                order.date_to = date_to
                order.sub_total = price
                order.save()
                messages.success(request, "Order Successful")
                return redirect("home")
            messages.error(request, "Unsuccessful Invalid information.")
        return render(request, 'bbq/bbqcheckout.html', {'order_form' : form, 'price': price})
    else:
        messages.warning(request, 'Please Log In')
        return redirect('view_bbq_rent', barbeque_id)


def checkout_calender(request, barbeque_id):
    if request.user.is_authenticated:
        form = CalenderForm()
        if request.method == "POST":
            form = CalenderForm(request.POST)
            if form.is_valid():
                messages.success(request, "Order Successful")
                request.session['date_from'] = form.data['date_from']
                request.session['date_to'] = form.data['date_to']
                request.session['delivery'] = form.data['delivery']
                request.session['pickup'] = form.data['pickup']
                return redirect("checkout_bbq", barbeque_id)
            messages.error(request, "Unsuccessful Invalid information.")
        return render(request, "bbq/calenderform.html", {'form': form})
    else:
        messages.warning(request, 'Please Log In')
        return redirect('view_bbq_rent', barbeque_id)

