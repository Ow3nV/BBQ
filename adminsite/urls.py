from django.urls import path
from . import views

urlpatterns = [
    path('site_admin', views.admin, name='admin'),
    path('bbq_form', views.create_bbq, name='admin_bbq_form'),
    path('admin_view', views.view_all_bbq, name='admin_view_all_bbqs'),
    path('bbq/<barbeque_id>', views.view_bbq, name='admin_view_bbq'),
    path('bbq/<barbeque_id>/edit', views.edit_bbq, name='admin_edit'),
    path('bbq_delete/<barbeque_id>', views.delete_bbq, name='bbq_delete'),
    path('allorders', views.view_orders, name='admin_all_orders'),
]