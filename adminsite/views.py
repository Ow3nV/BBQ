from django.contrib import messages
from django.shortcuts import render, redirect

from bbqweb.forms import BarbequeForm, BarbequeEditForm, ImageForm
from bbqweb.models import Barbeque, Images


# Create your views here.
def admin(request):
    if request.user.is_superuser:
        return render(request, 'admin/admin.html')
    else:
        return redirect('home')


def create_bbq(request):
    if request.method == "POST":
        form = BarbequeForm(request.POST, request.FILES)
        form2 = ImageForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            form.save()
            imgs = form2.save(commit=False)
            imgs.barbeque = Barbeque.objects.last()
            imgs.save()
            messages.success(request, "BBQ Added Successfully")
            return redirect("admin")
        messages.error(request, "Unsuccessful Invalid information.")
    form = BarbequeForm()
    form2 = ImageForm()
    if request.user.is_superuser:
        return render(request, "admin/bbqform.html", context={"register_form": form, "image_form": form2})
    else:
        return redirect('home')

def edit_bbq(request, barbeque_id):
    bbq = Barbeque.objects.get(id=barbeque_id)
    form = BarbequeEditForm(instance=bbq)
    if request.method == "POST":
        form = BarbequeForm(request.POST, instance=bbq)
        if form.is_valid():
            form.save()
            messages.success(request, "BBQ Added Successfully")
            return redirect("admin")
    return render(request, "admin/bbqedit.html", context={"register_form": form})




def view_all_bbq(request):
    bbqs = Barbeque.objects.all()
    return render(request, "admin/viewallbbq.html", {'bbqs': bbqs})


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

    return render(request, "admin/viewbbq.html", {'bbq': bbq, 'imgs': image_list})