# Generated by Django 5.1.5 on 2025-02-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0003_faq_translations"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faq",
            name="translations",
            field=models.JSONField(
                blank=True,
                help_text="Enter translations for multiple languages",
                null=True,
                verbose_name="Translations",
            ),
        ),
    ]
