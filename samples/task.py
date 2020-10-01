from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task():
    send_mail('Emailed the confirmation!!')
    
    return None
    