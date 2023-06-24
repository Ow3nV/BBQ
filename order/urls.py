from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<barbeque_id>', views.checkout_bbq, name='checkout_bbq'),
    path('selectdates/<barbeque_id>', views.checkout_calender, name='checkout_calender'),
    path('continueasguest/<barbeque_id>', views.checkout_guest, name='checkout_guest'),
    path('summary', views.summary, name='summary'),
]
