from rest_framework import mixins, viewsets


class CustomViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides default `create()`, `list()`, and `retrieve()` actions.
    """

    pass
