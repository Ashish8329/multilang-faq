from django.contrib import admin

from base.base_admin import BaseAdmin
from faq.models import FAQ


@admin.register(FAQ)
class FAQAdmin(BaseAdmin):
    list_display = ("question", "language", "created_at", "modified_at")
    search_fields = ("question",)
    list_filter = ("language",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "question",
                    "answer",
                    "language",
                )
            },
        ),
    )
