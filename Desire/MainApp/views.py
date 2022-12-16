from django.shortcuts import redirect, render
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import TemplateView, FormView

def index(request):

    if request.method == "POST" and 'login' in request.POST:
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, login_form.get_user())
                messages.info(request,'Успешный вход')
                return redirect('home')
            else:
                messages.error('Неверный логин или пароль')
        else:
            messages.error('Неверный логин или пароль')

    if request.method == "POST" and 'register' in request.POST:
        register_form = NewUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('home')

    register_form = NewUserForm
    login_form = LoginForm
    return render(request, 'index.html', context={
        'register_form':register_form,
        'login_form': login_form
    })
                    

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')

def blog(request):
    return render(request,'blog.html')

def contacts(request):
    return render(request, 'contacts.html')

def BlogConent(request):
    return render(request,'blog-one.html')



