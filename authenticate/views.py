from django.contrib.auth.decorators import login_required
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
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, template_name="auth/register.html", context={"register_form": form})

def login_user(request):
    form = LoginForm()
    # user login logic
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



def logout_view(request):
    logout(request)
    messages.success(request, "You are now logged out.")
    return redirect("home")


@login_required
def profile_view(request):
    return render(request, "auth/profile.html")
