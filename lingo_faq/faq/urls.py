from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path(
        "",
        views.FAQViewSet.as_view({"get": "list", "post": "create"}),
        name="faq-list",
    ),
]
