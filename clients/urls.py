from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as v
from django.contrib.auth import authenticate, login
from . import views
app_name="clients"
urlpatterns=[
    #homepage
    path('index/',views.index, name='index'),
    
    #login
    path('login/',v.LoginView.as_view(template_name='clients/login.html'), name='login'),
    
    
    #logout
    path('logout/', views.logout_view, name='logout'),
    
    #register
    path('register/',views.register, name='register'),
    
]
