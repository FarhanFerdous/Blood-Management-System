from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [
    path('requests/new/', views.request_create, name='request_create'),
    path('requests/', views.request_list, name='request_list'),
    path('donations/history/', views.donation_history, name='donation_history'),
]


