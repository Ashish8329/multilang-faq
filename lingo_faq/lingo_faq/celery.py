import os

from celery import Celery
from django.apps import apps

# Set default Django settings module for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lingo_faq.settings")

# Create Celery app
app = Celery("lingo_faq")

# Load settings from Django settings file
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks from all installed apps
app.autodiscover_tasks()
