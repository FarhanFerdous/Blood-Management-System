from rest_framework import viewsets, permissions, filters
from .models import BloodBank, BloodInventory
from .serializers import BloodBankSerializer, BloodInventorySerializer


class BloodBankViewSet(viewsets.ModelViewSet):
    queryset = BloodBank.objects.all()
    serializer_class = BloodBankSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "city"]


class BloodInventoryViewSet(viewsets.ModelViewSet):
    queryset = BloodInventory.objects.select_related("bank").all()
    serializer_class = BloodInventorySerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["blood_group", "bank__name", "bank__city"]


