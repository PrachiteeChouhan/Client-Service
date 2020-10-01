from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as v
from django.contrib.auth import authenticate, login
from . import views
app_name="service_providers"
urlpatterns=[
    #homepage
    path('index/',views.index, name='index'),
    path('login/',v.LoginView.as_view(template_name='service_providers/login.html'), name='login'),
     
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
    
    path('new_service/', views.new_service, name='new_service'),
]
