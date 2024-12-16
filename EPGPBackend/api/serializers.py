from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
        ]
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}
