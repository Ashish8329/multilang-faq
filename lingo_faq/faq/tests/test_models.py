import pytest
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.utils.translation import activate
from faq.models import FAQ
from faq.choices import LanguageChoices


@pytest.mark.django_db
def test_create_faq():
    """Test creating an FAQ instance"""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="<p>Django is a high-level Python web framework.</p>",
        language="en",
        translations={"es": {"question": "¿Qué es Django?", "answer": "<p>Django es un framework web en Python.</p>"}}
    )
    assert faq.id is not None
    assert faq.question == "What is Django?"
    assert faq.language == "en"


@pytest.mark.django_db
def test_default_language():
    """Test default language is English ('en')"""
    faq = FAQ.objects.create(
        question="What is AI?",
        answer="<p>AI stands for Artificial Intelligence.</p>"
    )
    assert faq.language == "en"

    
@pytest.mark.django_db
def test_faq_creation():
    # Create a FAQ instance with basic data
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="<p>Django is a high-level Python web framework.</p>",
        language=LanguageChoices.ENGLISH.value[0]
    )

    # Check that the FAQ was created successfully
    assert faq.question == "What is Django?"
    assert faq.answer == "<p>Django is a high-level Python web framework.</p>"
    assert faq.language == LanguageChoices.ENGLISH.value[0]
    assert faq.translations is None  # Initially translations should be None


@pytest.mark.django_db
def test_faq_with_translations():
    # Create FAQ with translations
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="<p>Django is a high-level Python web framework.</p>",
        language=LanguageChoices.ENGLISH.value[0],
        translations={"es": "Django es un marco web de Python de alto nivel."}
    )

    # Check that the translations are saved correctly
    assert "es" in faq.translations
    assert faq.translations["es"] == "Django es un marco web de Python de alto nivel."
