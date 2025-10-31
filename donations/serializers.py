from rest_framework import serializers
from .models import Donation, BloodRequest


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ["id", "donor", "bank", "units", "approved", "created_at"]
        read_only_fields = ["approved", "created_at"]


class BloodRequestSerializer(serializers.ModelSerializer):
    requester_username = serializers.ReadOnlyField(source="requester.username")

    class Meta:
        model = BloodRequest
        fields = [
            "id",
            "requester",
            "requester_username",
            "blood_group",
            "units",
            "reason",
            "status",
            "created_at",
        ]
        read_only_fields = ["status", "created_at", "requester"]


