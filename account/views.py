from django.shortcuts import render, redirect
from .forms import LogInForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import User


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'account/signUp.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated is True:
        return redirect('home:home')

    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:home')
    else:
        form = LogInForm()
    return render(request, "account/login.html", context={'form': form})


def log_out(request):
    logout(request)
    return redirect('home:home')
