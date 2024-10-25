from django.urls import path
from .views import (News, SeparateNews, NewsCreate, NewsUpdate, NewsDelete,
                    ArticleCreate, ArticleUpdate, ArticleDelete,
                    )

urlpatterns =[
    path('', News.as_view(), name='news'),
    path('<int:pk>', SeparateNews.as_view(), name='separate_news'),
    path('create/', NewsCreate.as_view(), name='create_news'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='update_news'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='delete_news'),
    path('articles/create/', ArticleCreate.as_view(),name='create_article'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='update_article'),
    path('articles/<int:pk>/delete', ArticleDelete.as_view(), name='delete_article'),
]