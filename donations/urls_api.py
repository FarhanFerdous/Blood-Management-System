from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import DonationViewSet, BloodRequestViewSet

app_name = 'donations_api'

router = DefaultRouter()
router.register('donations', DonationViewSet, basename='donation')
router.register('requests', BloodRequestViewSet, basename='bloodrequest')

urlpatterns = [
    path('', include(router.urls)),
]


