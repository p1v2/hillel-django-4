import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hillelDjango4.settings')


app = Celery('hillelDjango4')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()