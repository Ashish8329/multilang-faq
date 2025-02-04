import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from faq.models import FAQ

@pytest.mark.django_db
def test_get_faqs_default_language():
    """Test retrieving FAQs without specifying a language (default should be 'en')."""
    FAQ.objects.create(
        question="What is Django?",
        answer="<p>Django is a Python framework.</p>",
        language="en"
    )
    
    client = APIClient()
    url = reverse("faq-list")
    response = client.get(url)
    
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_faqs_with_language_filter():
    """Test retrieving FAQs with a specific language."""
    client = APIClient()
    url = "/api/v1/faq/?lang=en"
    response = client.get(url)
    
    assert response.status_code in [200, 204]
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert all(faq["language"] == "en" for faq in data)
        

@pytest.mark.django_db
def test_get_faqs_no_results():
    """Test retrieving FAQs when an invalid language is provided."""
    client = APIClient()
    url = "/api/v1/faq/?lang=fr"
    response = client.get(url)
    
    assert response.status_code == 400
    assert "Invalid language code" in response.json()