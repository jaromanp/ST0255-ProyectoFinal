from django.shortcuts import render

def Home(request):
    return render(request, 'Producto/index.html')
