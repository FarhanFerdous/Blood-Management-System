from django.contrib import admin
from .models import Donation, BloodRequest


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("donor", "bank", "units", "approved", "created_at")
    list_filter = ("approved", "bank")


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ("requester", "blood_group", "units", "status", "created_at")
    list_filter = ("status", "blood_group")

# Register your models here.
