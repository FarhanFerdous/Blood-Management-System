from django.db import models
from django.contrib.auth.models import User


class DonorProfile(models.Model):
    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"), ("A-", "A-"),
        ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"),
        ("O+", "O+"), ("O-", "O-"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="donor_profile")
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="donors/photos/", blank=True, null=True)
    last_donated_at = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username} ({self.blood_group})"


# Create your models here.
