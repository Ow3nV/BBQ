from django.urls import path
from . import views

urlpatterns = [
    path('site_admin', views.admin, name='admin'),
    path('bbq_form', views.create_bbq, name='admin_bbq_form'),
    path('admin_view', views.view_all_bbq, name='admin_view_all_bbqs'),
    path('bbq/<barbeque_id>', views.view_bbq, name='admin_view_bbq'),
]