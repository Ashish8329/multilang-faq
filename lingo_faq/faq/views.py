from django.shortcuts import render
from rest_framework import viewsets

from base.base_views import CustomViewSet

from .models import FAQ
from .serializers import FAQSerializer
from rest_framework.response import Response


class FAQViewSet(CustomViewSet):
    """
    A viewset that provides default `create()`, `list()`, and `retrieve()` actions.
    """

    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        """
        return a list of all the FAQs in the database with the request user's language.
        """
        param = request.query_params.get("lang")
        data = self.get_queryset()

        # serializer the data
        serialized_data = self.serializer_class(data, many=True).data

        if param:
            # itereate over the data
            # check if the param is in the translations
            if param == "en":
                return Response(serialized_data)
            
            #store the all the keys in trans;ation
            
            translation = []
            for faq in serialized_data:
                translation.extend(faq["translations"].keys())
            translations = set(translation)


            if param in translations:
                output_data = []
                for faq in serialized_data:
                    # add only the param key data to the translations
                    if param in faq["translations"]:
                        faq["translations"] = {param: faq["translations"].get(param)}
                        output_data.append(faq)
                return Response(output_data)

            else:
                serialized_data.append({"message": "No data found for the language"})
                return Response(serialized_data)
            
        return super().list(request, *args, **kwargs)