from rest_framework import serializers
from .models import DonorProfile


class DonorProfileSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = DonorProfile
        fields = [
            "id",
            "user",
            "user_username",
            "blood_group",
            "phone",
            "city",
            "available",
            "photo",
            "last_donated_at",
        ]
        read_only_fields = ["user"]


