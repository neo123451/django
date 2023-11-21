from django.urls import path
from .models import Post
from django.views.generic import ListView, DetailView


app_name = 'blogApp'
urlpatterns = [

    path('',ListView.as_view(
        queryset = Post.objects.all().order_by('-date')[:25],
        template_name ='blog.html'
    )),

    path('<int:pk>/',DetailView.as_view(
        model = Post,
        template_name = 'post.html'
    )),
]

