from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('rent', views.bbq_rent, name='rent_a_bbq'),
    path('', views.index, name=''),
    path('bbqrent/<barbeque_id>', views.view_bbq, name='view_bbq_rent'),
    path('rent_sort=low', views.bbq_rent_day, name='rent_a_bbq_low'),
    path('rent_sort=high', views.bbq_rent_day_high, name='rent_a_bbq_high'),
    path('rent_sort=name', views.bbq_rent_name, name='rent_a_bbq_name'),
]