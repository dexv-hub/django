from django.shortcuts import render
from django.http import HttpResponse
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
def login(request):
    return render(request, 'main/about.html')
def signup(request):
    return render(request, 'main/about.html')