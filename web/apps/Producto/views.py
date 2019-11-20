from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def Register(request):
    return render(request, 'Users/register.html')


class Inicio(TemplateView):
    template_name = 'index.html'
