from django.contrib import admin
from .models import BloodBank, BloodInventory


@admin.register(BloodBank)
class BloodBankAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "phone")
    search_fields = ("name", "city")


@admin.register(BloodInventory)
class BloodInventoryAdmin(admin.ModelAdmin):
    list_display = ("bank", "blood_group", "units_available")
    list_filter = ("blood_group",)

# Register your models here.
