from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from base.base_models import BaseModel
from faq.choices import LanguageChoices


class FAQ(BaseModel):
    question = models.TextField(
        max_length=255,
        verbose_name=_("Question"),
        help_text=_("Enter the question"),
    )
    answer = HTMLField(
        verbose_name=_("Answer"),
        help_text=_("Enter the answer"),
    )
    language = models.CharField(
        max_length=2,
        choices=[x.value for x in LanguageChoices],
        verbose_name=_("Language"),
        default=LanguageChoices.ENGLISH.value[0],
        help_text=LanguageChoices.get_help_text(),
    )

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
