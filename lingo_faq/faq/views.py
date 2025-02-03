from django.shortcuts import render
from rest_framework import viewsets

from base.base_views import CustomViewSet

from .models import FAQ
from .serializers import FAQSerializer


class FAQViewSet(CustomViewSet):
    """
    A viewset that provides default `create()`, `list()`, and `retrieve()` actions.
    """

    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
