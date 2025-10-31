from rest_framework import viewsets, permissions, filters
from .models import Donation, BloodRequest
from .serializers import DonationSerializer, BloodRequestSerializer


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.select_related("donor", "bank").all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]


class BloodRequestViewSet(viewsets.ModelViewSet):
    queryset = BloodRequest.objects.select_related("requester").all()
    serializer_class = BloodRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["blood_group", "status"]

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)


