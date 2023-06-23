from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from order.models import Order
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .models import UserAddress


def register_request(request):
    if request.user.is_anonymous:
        form = NewUserForm()
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = User.objects.last()
                address_line_1 = form.cleaned_data.get('address_line_1')
                address_line_2 = form.cleaned_data.get('address_line_2')
                town_city = form.cleaned_data.get('town_city')
                county = form.cleaned_data.get('county_state')
                country = form.cleaned_data.get('country')
                postcode = form.cleaned_data.get('postcode')
                address_data = UserAddress.objects.create(user=user, address_line_1=address_line_1,
                                                          address_line_2=address_line_2, town_city=town_city,
                                                          county_state=county, country=country, postcode=postcode)
                address_data.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("home")
            messages.error(request, "Unsuccessful registration. Invalid information.")
        return render(request, template_name="auth/register.html", context={"register_form": form})
    else:
        messages.warning(request, "You are already logged in")
        return redirect('home')


def login_user(request):
    if request.user.is_anonymous:
        form = LoginForm()
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You are now logged in.")
                    return redirect("home")
                else:
                    messages.error(request, 'Invalid credentials')

        return render(request, "auth/login.html", {"form": form})
    else:
        messages.warning(request, "You are already logged in")
        return redirect('home')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You are now logged out.")
        return redirect("home")
    messages.warning(request, "You are not logged in")
    return redirect('home')


def profile_view(request):
    if request.user.is_authenticated:
        return render(request, "auth/profile.html")
    messages.warning(request, "You are not logged in")
    return redirect('home')


def view_orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(email = request.user.email)
        return render(request, "auth/orders.html", {"orders": orders})
    messages.warning(request, "You are not logged in")
    return redirect('home')
