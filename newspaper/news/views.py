from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from datetime import datetime


# Create your views here.

class News(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

class SeparateNews(DetailView):
    model = Post
    template_name = 'separate_news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class CommentNews(DetailView):
    model = Comment
    template_name = 'separate_news.html'
    context_object_name = 'comment'
