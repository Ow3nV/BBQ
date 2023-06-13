from django.shortcuts import render, redirect
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, template_name="auth/register.html", context={"register_form": form})

def login_user(request):
    form = LoginForm()
    # user login logic
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in.")
                return redirect("index")
            else:
                messages.error(request, 'Invalid credentials')

    return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")
