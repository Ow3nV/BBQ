from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('rent', views.bbq_rent, name='rent_a_bbq'),
    path('', views.index, name=''),
    path('bbqrent/<barbeque_id>', views.view_bbq, name='view_bbq'),
]