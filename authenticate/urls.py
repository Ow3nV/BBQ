from django.urls import path

from authenticate import views

urlpatterns = [
    path('register', views.register_request, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile_view, name='profile'),
    path('vieworder', views.view_orders, name='view_order'),
]
