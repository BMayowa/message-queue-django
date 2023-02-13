# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters

from .serializers import PortfolioSerializer
from .models import *
from .serializers import *
from .producer import publish


class PortfolioViewSets(viewsets.ModelViewSet):
    """Portfolio view sets"""

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    http_method_names = ["get", "post"]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]

    def perform_create(self, serializer):
        publish("portfolio_created", serializer.data)
        print("Published portfolio")
        return

    def perform_update(self, serializer):
        publish("portfolio_updated", serializer.data)
        return
