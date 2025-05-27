from celery import Celery
from celery.schedules import crontab

app = Celery("your_project")  # Replace with your project name
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-newsletter-every-week": {
        "task": "your_app.tasks.send_newsletter",
        "schedule": crontab(minute=0, hour=8, day_of_week=1),  # Monday 8 AM
    },
}
