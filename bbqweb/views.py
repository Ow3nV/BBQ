from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from bbqweb.forms import BarbequeForm
from bbqweb.models import Barbeque, Images
from order.forms import OrderForm
from order.models import Order


# Create your views here.
def index(request):
    return redirect('home')


def home(request):
    return render(request, 'bbq/bbqhome.html')


def bbq_rent(request):
    search = request.GET.get('query')
    sort_option = request.GET.get('sort')

    if sort_option == 'high':
        queryset = Barbeque.objects.order_by('-rent')
    elif sort_option == 'low':
        queryset = Barbeque.objects.order_by('rent')
    elif sort_option == 'name':
        queryset = Barbeque.objects.order_by('name')
    else:
        queryset = Barbeque.objects.all()

    if search:
        queryset = queryset.filter(name__icontains=search)

    gas_filter = request.GET.get('gas')
    burners_filter = request.GET.get('burners')
    price_min_filter = request.GET.get('price_min')
    price_max_filter = request.GET.get('price_max')

    if gas_filter:
        queryset = queryset.filter(gas=gas_filter)
    if burners_filter:
        queryset = queryset.filter(burners=burners_filter)
    if price_min_filter and price_max_filter:
        queryset = queryset.filter(rent__gte=price_min_filter, rent__lte=price_max_filter)
    elif price_min_filter:
        queryset = queryset.filter(rent__gte=price_min_filter)
    elif price_max_filter:
        queryset = queryset.filter(rent__lte=price_max_filter)

    context = {
        'bbqs': queryset,
        'search': search,
        'filter_gas': gas_filter,
        'filter_burners': burners_filter,
        'filter_price_min': price_min_filter,
        'filter_price_max': price_max_filter,
        'sort_option': sort_option
    }

    return render(request, "bbq/bbqrent.html", context)


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


def check_id_exists(id_number, dictionary):
    for key, value in dictionary.items():

        if key == id_number:
            return True
    return False


def add_to_cart(request, barbeque_id):
    bbq = Barbeque.objects.get(id=barbeque_id)

    # Retrieve the BBQ name from the query parameters
    bbq_name = bbq.name

    # Get the cart from the session or create a new one if it doesn't exist
    cart = request.session.get('cart', {})

    # Add the BBQ ID and name to the cart dictionary

    if check_id_exists(barbeque_id, cart):
        error_message = "Duplicate"
        return HttpResponse(error_message, status=400)
    else:
        print(f"Thasddfadfasdfionary.")
        cart[barbeque_id] = bbq_name

        # Store the updated cart back in the session
        request.session['cart'] = cart

        # Output the updated cart to verify
        #print('Cart:', cart)

        # Redirect the user to the desired page after adding to the cart
        return JsonResponse({'cart': cart})
        #return HttpResponse()



def remove_from_cart(request, barbeque_id):
    del request.session['cart'][barbeque_id]
    request.session.modified = True
    imgs = []
    for item in request.session['cart']:
        img = Barbeque.objects.get(id=item).image.url
        imgs.append(img)
    return JsonResponse({'cart': request.session['cart'], 'images': imgs})


def remove_from_final_cart(request, barbeque_id):
    bbq = Barbeque.objects.get(id=barbeque_id).image
    del request.session['cart'][barbeque_id]
    request.session.modified = True
    print(bbq.url)
    return JsonResponse({'cart': request.session['cart'], 'image':bbq.url})


def view_cart(request):
    return request.session['cart']


def view_availability(request, barbeque_id):
    bbq = Barbeque.objects.get(id=barbeque_id)
    all_dates = Order.objects.filter(barbeque=bbq)
    order_events = []

    for order in all_dates:
        date_from = order.date_from
        date_to = order.date_to + timedelta(days=1)  # Include the end date in the range
        order_events.append({
            'title': bbq.name,  # Event title
            'start': date_from.strftime('%Y-%m-%d'),  # Start date
            'end': date_to.strftime('%Y-%m-%d'),  # End date (next day)
        })
    return render(request, "bbq/bbqavailability.html", {'events': order_events})

def get_bbq_image(request, bbq_id):
    bbq = get_object_or_404(Barbeque, id=bbq_id)
    image_url = bbq.image.url  # Assuming the Barbeque model has an 'image' field

    return JsonResponse({'image_url': image_url})