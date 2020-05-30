from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import ListView, TemplateView, View
from .forms import ArticleForm


def articles(request):
    return render(request, 'articles.html')


class ArticlesList(ListView):
    model = Articles



def write_article(request):
    if request.user.is_authenticated:
        form = ArticleForm()
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.createdBy = request.user
                post.save()
                return redirect('articles')
        context = {'form': form}
        return render(request, 'write_article.html', context)

    else:
        return redirect('../../authentication/login')