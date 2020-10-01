from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ServiceProviderForm


def index(request):
    return render(request, 'service_providers/index.html')

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "users/login_request.html",
                  context={"form":form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('samples:index'))

def register(request):
    if request.method != 'POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user=form.save()
            authenticate_user=authenticate(username=new_user.username, password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('samples:service_provider'))
    context={'form':form}
    return render(request,'service_providers/register.html',context)



def new_service(request):
    if request.method!= 'POST':
        form=ServiceProviderForm()
    
    else:
        form=ServiceProviderForm(data=request.POST)
        if form.is_valid():
            new_service=form.save(commit=False)
            new_service.owner=request.user
            new_service.save()
            
            return HttpResponseRedirect(reverse('samples:service_provider'))
    context={'form':form}
    return render(request,'service_providers/new_service.html',context)