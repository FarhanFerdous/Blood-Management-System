from django.db import models


class BloodBank(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class BloodInventory(models.Model):
    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"), ("A-", "A-"),
        ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"),
        ("O+", "O+"), ("O-", "O-"),
    ]

    bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE, related_name="inventories")
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    units_available = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("bank", "blood_group")

    def __str__(self) -> str:
        return f"{self.bank.name} - {self.blood_group}: {self.units_available} units"


# Create your models here.
