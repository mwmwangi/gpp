from celery import shared_task
from django.core.mail import send_mail
from .models import Subscriber

@shared_task
def send_newsletter():
    subscribers = Subscriber.objects.values_list('email', flat=True)
    subject = "Weekly Marketing Tips"
    message = "Here’s your weekly dose of marketing tips!"
    from_email = "your@email.com"  # Replace with your email

    if subscribers:
        send_mail(subject, message, from_email, subscribers)

    return f"Newsletter sent to {len(subscribers)} subscribers."
