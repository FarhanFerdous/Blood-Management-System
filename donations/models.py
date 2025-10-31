from django.db import models
from django.contrib.auth.models import User
from donors.models import DonorProfile
from banks.models import BloodBank


class Donation(models.Model):
    donor = models.ForeignKey(DonorProfile, on_delete=models.CASCADE, related_name="donations")
    bank = models.ForeignKey(BloodBank, on_delete=models.SET_NULL, null=True, blank=True)
    units = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Donation by {self.donor.user.username} ({self.units} units)"


class BloodRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3)
    units = models.PositiveIntegerField(default=1)
    reason = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Request {self.blood_group} x{self.units} by {self.requester.username} ({self.status})"


# Create your models here.
