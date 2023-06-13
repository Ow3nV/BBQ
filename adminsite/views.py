from django.contrib import messages
from django.shortcuts import render, redirect

from bbqweb.forms import BarbequeForm
from bbqweb.models import Barbeque


# Create your views here.
def admin(request):
    if request.user.is_superuser:
        return render(request, 'admin/admin.html')
    else:
        return redirect('home')


def create_bbq(request):
    if request.method == "POST":
        form = BarbequeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "BBQ Added Successfully")
            return redirect("admin")
        messages.error(request, "Unsuccessful Invalid information.")
    form = BarbequeForm()
    if request.user.is_superuser:
        return render(request, "admin/bbqform.html", context={"register_form": form})
    else:
        return redirect('home')


def view_all_bbq(request):
    bbqs = Barbeque.objects.all()
    return render(request, "admin/viewallbbq.html", {'bbqs': bbqs})


def view_bbq(request, barbeque_id):
    bbq = Barbeque.objects.get(id=barbeque_id)
    return render(request, "admin/viewbbq.html", {'bbq': bbq})