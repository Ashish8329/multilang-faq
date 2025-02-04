from django.db.models.signals import post_save
from django.dispatch import receiver

from faq.models import FAQ


@receiver(post_save, sender=FAQ)
def create_faq_translation(sender, instance, created, **kwargs):
    """
    Using djngo signals to create translations for the FAQ model
    """
    if created:  # TODO celery task regostration
        instance.translations = {
            instance.language: {
                "question": instance.question,
                "answer": instance.answer,
            }
        }
        instance.save()
