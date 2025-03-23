from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Register


def met(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def event_details(request):
    return render(request,'main/details.html')
def tickets(request):
    return render(request, 'main/tickets.html')
def donate(request):
    return render(request, 'main/donate.html')
def signup(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Your information is incorrect'

    form = RegisterForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/signup.html', data)


def login(request):
    return render(request, 'main/login.html')
