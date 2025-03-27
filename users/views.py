from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserLoginForm, RegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully registered')
            return HttpResponseRedirect(reverse('login'))
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)

def profile(request):
    form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/profile.html', context)