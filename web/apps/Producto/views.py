from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm
from django.template import RequestContext

#from django.contrib.auth.decorators import login_requiered

def index(request):
    return render(request, 'index.html')


def Register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit = False)

            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')
        else:
            form = ExtendedUserCreationForm()
            profile_form = UserProfileForm()

        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'Users/register.html', context_instance=RequestContext(request))



class Inicio(TemplateView):
    template_name = 'index.html'
