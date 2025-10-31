from django.urls import path
from . import views

app_name = 'donors'

urlpatterns = [
    path('profile/', views.profile_edit, name='profile_edit'),
    path('donors/', views.donor_search, name='search'),
]


