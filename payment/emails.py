# In your_app/emails.py
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(user_email):
    subject = 'Your purchase confirmation'
    message = 'Thank you for your purchase!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)
