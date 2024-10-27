from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(user_email, order_number):
    subject = 'Your purchase confirmation'
    message = f'Thank you for your purchase! Your order number is {order_number}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)
