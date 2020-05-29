from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def mainpage(reques):
    context = {}
    return render(reques, 'mainpage.html', context)
