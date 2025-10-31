from django.urls import path
from . import views

app_name = 'dashboards'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/donor/', views.donor_dashboard, name='donor_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('demo/', views.demo_walkthrough, name='demo_walkthrough'),
    path('demo/action/create-request/', views.demo_create_request, name='demo_create_request'),
    path('demo/action/approve-request/', views.demo_approve_request, name='demo_approve_request'),
    path('demo/action/create-donation/', views.demo_create_donation, name='demo_create_donation'),
]


