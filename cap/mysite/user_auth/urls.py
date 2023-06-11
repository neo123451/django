from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [

    path('home/',views.Home, name='Home'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path("register", views.register_request, name="register"),
    path('', views.login_request, name='Login')





]
