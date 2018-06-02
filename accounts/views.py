from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegistrationForm


def login_view(request):
    template = 'accounts/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,
                            password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect ('/')
        form = AuthenticationForm(request.POST)
        return render(request, template, {'form': form})
    if request.user.is_authenticated:
        return redirect('/')
    form = AuthenticationForm()
    return render(request, template, {'form': form})


def register(request):
    template = 'accounts/register.html'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = request.POST['email']
            # password = request.POST['password1']
            # print("-"*50)
            # print(username, password)
            # user = authenticate(username=username,
            #                     password=password)
            # login(request, user)
            return redirect('/')
        return render(request, template, {'form': form})
    form = RegistrationForm()
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, template, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def profile(request):
    template = 'accounts/profile.html'
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            print('*'*50)
            print(request.path)
            return redirect(request.path)
    form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, template, context)