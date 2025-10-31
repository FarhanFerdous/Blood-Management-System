from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import BloodBankViewSet, BloodInventoryViewSet

app_name = 'banks_api'

router = DefaultRouter()
router.register('banks', BloodBankViewSet, basename='bank')
router.register('inventory', BloodInventoryViewSet, basename='inventory')

urlpatterns = [
    path('', include(router.urls)),
]


