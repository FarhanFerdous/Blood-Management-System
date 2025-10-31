from django.contrib import admin
from .models import DonorProfile


@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "blood_group", "city", "available")
    search_fields = ("user__username", "city", "blood_group")
    list_filter = ("blood_group", "available", "city")

# Register your models here.
