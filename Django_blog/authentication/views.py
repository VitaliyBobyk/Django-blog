from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    """Перевірка чи користувач залогінений
        Якщо він залогінений то спрацьовує редірект на головну сторінку(для унеможливлення
        відображення сторінки логіну)
    """
    if request.user.is_authenticated:
        return redirect('mainpage')
    else:
        """Отримуємо ім'я користувача та пароль"""
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            """Якщо користувач є в БД то робимо редірект на головну сторінку"""
            if user is not None:
                login(request, user)
                return redirect("http://127.0.0.1:8000/")
            else:
                messages.info(request, 'Username or passwords is incorrect!')
        context = {}
        return render(request, 'login.html', context)


def register(request):
    """Перевірка чи користувач залогінений
            Якщо він залогінений то спрацьовує редірект на головну сторінку(для унеможливлення
            відображення сторінки реєстрації)"""
    if request.user.is_authenticated:
        return redirect('mainpage')
    else:
        """Отримуємо форму в яку будуть записані дані з форм  які знаходять в темплейті"""
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            """Якщо форма проходить валідацію то записуємо дані в БД"""
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
    context = {'form': form}
    return render(request, 'signup.html', context)

"""При виході з акаунту користувача робимо редірект на сторінку входу"""
def logoutUser(request):
    logout(request)
    return redirect('login')


