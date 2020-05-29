from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
from django.views.generic import ListView


def articles(request):
    return render(request, 'articles.html')

#
class ArticlesList(ListView):
    model = Articles