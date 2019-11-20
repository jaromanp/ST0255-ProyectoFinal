from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def Login(request):
    return render(request, 'Login/login.html')