from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def Home(request):
    return render(request, 'Producto/index.html')


def register(reques):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

