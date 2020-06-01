from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import ListView, TemplateView, View
from .forms import ArticleForm


def articles(request):
    return render(request, 'articles.html')


class ArticlesList(ListView):
    """Отримання моделі"""
    model = Articles


def write_article(request):
    """Перевірка чи користувач залогінений"""
    if request.user.is_authenticated:
        form = ArticleForm()
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                """Запис нового поста в БД"""
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('articles')
        context = {'form': form}
        return render(request, 'write_article.html', context)

    else:
        return redirect('../../authentication/login')


def like_article(request):
    """Перевірка чи користувач залогінений"""
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            """Отримання користувача та перевірка на наявність лайку на даному пості"""
            article_id = request.POST.get('article_id')
            article_obj = Articles.objects.get(id=article_id)
            if user in article_obj.liked.all():
                article_obj.liked.remove(user)
                return redirect('articles')
            else:
                article_obj.liked.add(user)
                return redirect('articles')
    else:
        return redirect('articles')

