from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView
                                  )
from django.urls import reverse_lazy
from .models import Post, Comment
from datetime import datetime
from .filters import NewsFilter
from .forms import NewsForm


# Create your views here.

class News(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
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

class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'create_news.html'
    success_url = reverse_lazy('create_news')

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/create/':
            post.categoryType = 'NW'
        post.save()
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'edit_news.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class NewsDelete(DeleteView):
    model = Post
    template_name = 'delete_news.html'
    success_url = reverse_lazy('news')


class ArticleCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'create_article.html'
    success_url = reverse_lazy('create_article')


class ArticleUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'edit_article.html'
    success_url = reverse_lazy('news')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('news')

