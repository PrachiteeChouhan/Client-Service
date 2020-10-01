
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404,HttpResponse
from django.urls import reverse

from .models import Service_Provider
from .task import send_email_task


def index(request):
    """index page"""
    return render(request, 'samples/index.html')


def service_provider(request):
    """display all services by the particular service provider"""
    
    service=Service_Provider.objects.filter(owner=request.user).order_by('date_added')
    #if service.owner != request.user:
    #    raise Http404
    context={'service':service}
    return render(request,'samples/service_provider.html',context)


def service_providers(request):
    """display all service provider"""
    services=Service_Provider.objects.all()
    
    context={'services':services}
    return render(request,'samples/service_providers.html',context)


def send_email(request):
    """to send email through celery"""
    send_email_task.delay()
    return HttpResponse("Email Sent!!")