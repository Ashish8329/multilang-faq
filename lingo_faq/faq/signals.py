from django.db.models.signals import post_save
from django.dispatch import receiver

from faq.models import FAQ
from faq.tasks import start_translation


@receiver(post_save, sender=FAQ)
def create_faq_translation(sender, instance, created, **kwargs):
    """
    Using django signals to create translations for the FAQ model
    """
    if created:
        start_translation.delay( 
            instance.id, instance.question, instance.answer, instance.language
        )  # ASYNC CALL
