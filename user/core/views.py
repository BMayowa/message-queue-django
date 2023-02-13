# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters

from core.serializers import ListUserSerializer


class UserViewSets(viewsets.ModelViewSet):
    """User view sets"""

    queryset = get_user_model().objects.all()
    serializer_class = ListUserSerializer
    http_method_names = ["get", "post"]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["email", "first_name", "last_name", "phone"]
    ordering_fields = [
        "last_login",
        "email",
        "first_name",
        "last_name",
        "phone",
    ]
