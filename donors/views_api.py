from rest_framework import viewsets, permissions, filters
from .models import DonorProfile
from .serializers import DonorProfileSerializer


class IsSelfOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user


class DonorProfileViewSet(viewsets.ModelViewSet):
    queryset = DonorProfile.objects.select_related("user").all()
    serializer_class = DonorProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["blood_group", "city", "user__username"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.IsAuthenticated()]
        return [IsSelfOrAdmin()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


