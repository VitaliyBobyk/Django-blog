from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView


def articles(request):
    return render(request, 'articles.html')


class ArticlesList(ListView):
    model = Articles


def write_article(reques):
    return render(reques, 'write_article.html')