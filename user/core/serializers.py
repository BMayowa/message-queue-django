from django.contrib.auth import get_user_model
from rest_framework import serializers


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "last_login",
            "portfolio_count",
        ]
