from django.urls import path
from .views import index
from .views import Login
from .views import Register

urlpatterns = [
    path('', index, name = 'index'),
    path('login/', Login, name='Login'),
    path('register/', Register, name='Register')
]

