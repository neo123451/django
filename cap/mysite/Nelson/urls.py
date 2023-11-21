from django.urls import path
from . import views

app_name = "Nelson"

urlpatterns = [
    path('bio/',views.bio, name = 'bio'),
    path('background/', views.background, name = "background"),
    path('campaign/', views.campaign, name  = "campaign"),
]
