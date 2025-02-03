# Generated by Django 5.1.5 on 2025-02-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0002_alter_faq_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="faq",
            name="translations",
            field=models.JSONField(
                default=dict,
                help_text="Enter translations for multiple languages",
                verbose_name="Translations",
            ),
        ),
    ]
