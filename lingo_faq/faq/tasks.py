import logging

from celery import shared_task

logger = logging.getLogger(__name__)  # Create a logger


@shared_task
def test_celery(x, y):
    z = x + y
    print(f"----------------{z}----------------")
    return z
