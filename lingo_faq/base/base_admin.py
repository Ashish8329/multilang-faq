from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    exclude = [
        "deleted_at",
    ]
    readonly_fields = ("created_at", "modified_at")
