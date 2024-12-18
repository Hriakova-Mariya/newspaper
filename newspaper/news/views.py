from django.contrib.auth.models import Group

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Post, Comment, Subscription, Category, Author
from datetime import datetime
from .filters import NewsFilter
from .forms import NewsForm
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView
                                  )
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

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
    context_object_name = 'separate_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class CommentNews(DetailView):
    model = Comment
    template_name = 'separate_news.html'
    context_object_name = 'comment'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    raise_exception = True
    form_class = NewsForm
    model = Post
    template_name = 'create_news.html'
    success_url = reverse_lazy('separate_news')

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/create/':
            post.categoryType = 'NW'
        post.save()
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'edit_news.html'
    success_url = reverse_lazy('separate_news')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'delete_news.html'
    success_url = reverse_lazy('news')


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'create_article.html'
    success_url = reverse_lazy('separate_news')


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'edit_article.html'
    success_url = reverse_lazy('separate_news')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('news')

@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(
                user=request.user,
                category=category
            )
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('id')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )

@login_required
@csrf_protect
def be_author(self, request):
    if request.method == 'POST':
        group_id = request.Group.get('group_id')
        group_authors =
        action = request.POST.get('action')
        if action == 'subscribe':
            user=super().save(request)
            authors = Group.objects.get(name="authors")
            user.groups.add(authors)
    return render(
        request,
        'be_author.html',
    )