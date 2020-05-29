from django.urls import path, include
from . import views
from .views import ArticlesList


urlpatterns = [
    path('', ArticlesList.as_view(template_name='articles.html')),
    path('', views.articles, name='articles')
]