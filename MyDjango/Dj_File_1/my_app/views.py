from django.shortcuts import render

from .models import *
from django.views.generic import ListView, DetailView


class ListPost(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'List_Posts.html'
    context_object_name = 'listPosts'


class OnePost(DetailView):
    model = Post
    template_name = 'One_Post.html'
    context_object_name = 'onePost'
