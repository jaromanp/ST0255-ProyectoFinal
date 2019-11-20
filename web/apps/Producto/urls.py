from django.urls import path, include
from .views import index
from .views import Register


urlpatterns = [
    path('', index, name = 'index'),
    path('register/', Register, name='Register')
]

