from time import strftime

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date

from authenticate.models import UserAddress
from bbqweb.models import Barbeque
from order.forms import OrderForm, CalenderForm
from order.models import Order
import pandas


# Create your views here.

def checkout_bbq(request, barbeque_id):
    if request.user.is_authenticated:
        address_fields = UserAddress.objects.get(user=request.user)
        form = OrderForm(initial={'email': request.user.email, 'name': request.user.get_full_name(),
                                  'address_line_1': address_fields.address_line_1,
                                  'address_line_2': address_fields.address_line_2,
                                  'town_city': address_fields.town_city, 'county_state': address_fields.county_state,
                                  'country': address_fields.country, 'postcode': address_fields.postcode})
        date_from = parse_date(request.session['date_from'])
        date_to = parse_date(request.session['date_to'])
        delivery = request.session['delivery']
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
        return render(request, 'bbq/bbqcheckout.html', {'order_form': form, 'price': price})
    else:
        messages.warning(request, 'Please Log In')
        return redirect('view_bbq_rent', barbeque_id)


def checkout_calender(request, barbeque_id):
    if request.user.is_authenticated:
        bbq = Barbeque.objects.get(id=barbeque_id)
        order_dates = Order.objects.filter(barbeque=bbq)
        all_dates = []
        for dates in order_dates:
            date_range = pandas.date_range(dates.date_from, dates.date_to, freq="d")
            all_dates.extend(date_range.strftime("%Y-%m-%d"))
        all_dates = list(dict.fromkeys(all_dates))
        form = CalenderForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                selected_date_range = request.POST['date_range']
                selected_date_range = selected_date_range.split(" to ")
                messages.success(request, "Booking Available")
                request.session['date_from'] = selected_date_range[0]
                request.session['date_to'] = selected_date_range[-1]
                request.session['delivery'] = form.cleaned_data['delivery']
                request.session['pickup'] = form.cleaned_data['pickup']
                return redirect("checkout_bbq", barbeque_id)
            messages.error(request, "Unsuccessful Invalid information.")
        return render(request, "bbq/calenderform.html", {'form': form, 'unavailable_dates': all_dates})
    else:
        messages.warning(request, 'Please Log In')
        return redirect('view_bbq_rent', barbeque_id)
