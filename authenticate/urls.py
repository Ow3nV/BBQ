from django.urls import path

from authenticate import views

urlpatterns = [
    path('register', views.register_request, name='register'),
    path('login', views.login_user, name='login'),
]
