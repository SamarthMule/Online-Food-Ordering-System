
from django.shortcuts import render

def login_view(request):
    return render(request, 'authentication/login.html')

def registration_view(request):
    return render(request, 'authentication/registration.html')
