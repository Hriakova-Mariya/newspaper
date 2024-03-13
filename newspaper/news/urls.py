from django.urls import path
from .views import News, SeparateNews

urlpatterns =[
    path('', News.as_view()),
    path('<int:pk>', SeparateNews.as_view())
]