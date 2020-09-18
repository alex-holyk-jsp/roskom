from django.core.mail import send_mail
from django.conf import settings


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split('.')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def send_email(receiver_email):
    subject = 'Your domain was blocked'
    message = 'Congrats! The requested domain was blocked'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [receiver_email,]

    send_mail(subject, message, email_from, recipient_list)
