import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_shop.settings")

broker_url = "amqp://admin:admin@localhost:5672//"

app = Celery("django_shop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
