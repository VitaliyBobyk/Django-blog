from django.shortcuts import render


def mainpage(reques):
    context = {}
    return render(reques, 'mainpage.html', context)
