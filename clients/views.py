from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    """index page for client"""
    return render(request, 'clients/index.html')




def logout_view(request):
    """logout view"""
    logout(request)
    return HttpResponseRedirect(reverse('samples:index'))

def register(request):
    """register view"""
    if request.method != 'POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user=form.save()
            authenticate_user=authenticate(username=new_user.username, password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('samples:service_providers'))
    context={'form':form}
    return render(request,'clients/register.html',context)