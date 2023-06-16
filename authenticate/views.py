from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import NewUserForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register_request(request):
    if request.user.is_anonymous:
        form = NewUserForm()
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
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
