from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import DonorProfileViewSet

app_name = 'donors_api'

router = DefaultRouter()
router.register('profiles', DonorProfileViewSet, basename='donorprofile')

urlpatterns = [
    path('', include(router.urls)),
]


