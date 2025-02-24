from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from base.base_views import CustomViewSet
from faq.choices import LanguageChoices

from .models import FAQ
from .serializers import FAQSerializer
from .utils import filter_by_language


class FAQViewSet(CustomViewSet):
    """
    A viewset that provides default `create()`, `list()`, and `retrieve()` actions.
    """

    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        """
        Return a list of all the FAQs in the database with the requested language.
        """
        param = request.query_params.get("lang")

        if param:
            # get lanugage code from the enum  chiuces
            lang_codes = [lang[0] for lang in LanguageChoices.choices()]

            # check if the language code is valid
            if param not in lang_codes:
                raise ValidationError("Invalid language code")

        data = self.get_queryset()
        serialized_data = self.serializer_class(data, many=True).data

        # If the 'lang' parameter is provided, filter accordingly
        if param:

            cache_key = f"faq_{param}"
            cached_data = cache.get(cache_key)

            # check if the data is in the cache
            if cached_data:
                return Response(cached_data)

            if param == "en":
                # Filter by 'en' translations
                output_data = filter_by_language(serialized_data, "en")
                cache.set(cache_key, output_data, 60)
                return Response(output_data)

            # Collect all available translation keys
            translations = {
                key for faq in serialized_data for key in faq["translations"].keys()
            }

            if param in translations:
                # Filter by the requested language
                output_data = filter_by_language(serialized_data, param)
                cache.set(cache_key, output_data, 60)
                return Response(output_data)

            else:
                # If the language is not found, return a message with filter by 'en' by default
                output_data = filter_by_language(serialized_data, "en")
                output_data.append({"message": "No data found for the language"})
                cache.set(cache_key, output_data, 60)
                return Response(output_data)

        # If no 'lang' parameter is provided, filter by 'en' by default
        output_data = filter_by_language(serialized_data, "en")
        return Response(output_data)
