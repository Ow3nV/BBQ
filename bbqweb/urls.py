from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('rent', views.bbq_rent, name='rent_a_bbq'),
    path('', views.index, name=''),
    path('bbqrent/<barbeque_id>', views.view_bbq, name='view_bbq_rent'),
    path('add_to_cart/<barbeque_id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<barbeque_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_from_final_cart/<barbeque_id>/', views.remove_from_final_cart, name='remove_from_final_cart'),
    path('availability/<barbeque_id>/', views.view_availability, name='bbq_availability'),
]
