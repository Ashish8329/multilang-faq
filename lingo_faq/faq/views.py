from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from base.base_views import CustomViewSet

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
        data = self.get_queryset()
        serialized_data = self.serializer_class(data, many=True).data

        # If the 'lang' parameter is provided, filter accordingly
        if param:
            if param == "en":
                # Filter by 'en' translations
                output_data = filter_by_language(serialized_data, "en")
                return Response(output_data)

            # Collect all available translation keys
            translations = {
                key for faq in serialized_data for key in faq["translations"].keys()
            }

            if param in translations:
                # Filter by the requested language
                output_data = filter_by_language(serialized_data, param)
                return Response(output_data)
            else:
                # If the language is not found, return a message with filter by 'en' by default
                output_data = filter_by_language(serialized_data, "en")
                output_data.append({"message": "No data found for the language"})
                return Response(output_data)

        # If no 'lang' parameter is provided, filter by 'en' by default
        output_data = filter_by_language(serialized_data, "en")
        return Response(output_data)
