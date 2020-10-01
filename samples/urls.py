from django.urls import path
from . import views

app_name="samples"
urlpatterns=[
    #homepage
    path('',views.index, name='index'),
    
    #to display the service provider offers
    path('service_provider/', views.service_provider, name='service_provider'),
    
    #to display clients
    path('service_providers/', views.service_providers, name='service_providers'),
    
    #for sending confirmation emails
    path('send_email/', views.send_email, name='send_email'),
    
    
    
]