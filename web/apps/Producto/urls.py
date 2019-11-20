from django.urls import path
from .views import index
from .views import Login

urlpatterns = [
    path('', index, name = 'index'),
    path('login', Login, name='Login')
]

