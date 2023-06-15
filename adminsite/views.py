from django.contrib import messages
from django.shortcuts import render, redirect

from bbqweb.forms import BarbequeForm, ImageForm
from bbqweb.models import Barbeque, Images


# Create your views here.
def admin(request):
    if request.user.is_superuser:
        return render(request, 'admin/admin.html')
    else:
        messages.warning(request, "No Access")
        return redirect('home')


def create_bbq(request):
    if request.user.is_superuser:
        form = BarbequeForm()
        form2 = ImageForm()
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
        return render(request, "admin/bbqform.html", context={"register_form": form, "image_form": form2})
    else:
        messages.warning(request, "No Access")
        return redirect('home')


def edit_bbq(request, barbeque_id):
    if request.user.is_superuser:
        bbq = Barbeque.objects.get(id=barbeque_id)
        imgbbq = Images.objects.get(barbeque=bbq)
        form = BarbequeForm(instance=bbq)
        form2 = ImageForm(instance=imgbbq)
        if request.method == "POST":
            form = BarbequeForm(request.POST, request.FILES, instance=bbq)
            form2 = ImageForm(request.POST, request.FILES, instance=imgbbq)
            if form.is_valid():
                form.save()
                form2.save()
                messages.success(request, "BBQ Added Successfully")
                return redirect("admin")
        return render(request, "admin/bbqedit.html", context={"register_form": form, "image_form": form2})
    else:
        messages.warning(request, "No Access")
        return redirect('home')




def view_all_bbq(request):
    if request.user.is_superuser:
        bbqs = Barbeque.objects.all()
        return render(request, "admin/viewallbbq.html", {'bbqs': bbqs})
    else:
        messages.warning(request, "No Access")
        return redirect('home')


def view_bbq(request, barbeque_id):
    if request.user.is_superuser:
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
    else:
        messages.warning(request, "No Access")
        return redirect('home')


def delete_bbq(request, barbeque_id):
    if request.user.is_superuser:
        Barbeque.objects.get(id=barbeque_id).delete()
        messages.success(request, "BBQ deleted")
        return redirect('admin_view_all_bbqs')
    else:
        messages.warning(request, "No Access")
        return redirect('home')
