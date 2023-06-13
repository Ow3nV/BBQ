from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('rent', views.bbq_rent, name='rent_a_bbq'),
    path('', views.index, name=''),
    path('site_admin', views.admin, name='admin'),
    path('bbq_form', views.create_bbq, name='bbq_form'),
    path('view_all_bbqs', views.view_all_bbq, name='view_all_bbqs'),
    path('adminbbq/<barbeque_id>', views.view_bbq, name='view_bbq'),
]