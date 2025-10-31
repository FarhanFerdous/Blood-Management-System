from rest_framework import serializers
from .models import BloodBank, BloodInventory


class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = ["id", "name", "address", "city", "phone"]


class BloodInventorySerializer(serializers.ModelSerializer):
    bank = BloodBankSerializer(read_only=True)
    bank_id = serializers.PrimaryKeyRelatedField(
        queryset=BloodBank.objects.all(), source="bank", write_only=True
    )

    class Meta:
        model = BloodInventory
        fields = ["id", "bank", "bank_id", "blood_group", "units_available"]


