from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from donors.models import DonorProfile
from banks.models import BloodBank, BloodInventory


class Command(BaseCommand):
    help = "Seed demo users, donor profiles, and sample bank/inventory"

    def handle(self, *args, **options):
        # Admin
        admin, _ = User.objects.get_or_create(
            username="admin",
            defaults={"email": "admin@example.com", "is_staff": True, "is_superuser": True},
        )
        admin.set_password("Admin@123")
        admin.save()

        # Staff
        staff, _ = User.objects.get_or_create(
            username="staff",
            defaults={"email": "staff@example.com", "is_staff": True},
        )
        staff.set_password("Staff@123")
        staff.save()

        # Donors
        demo_donors = [
            ("donor1", "Donor1@123", "A+", "01700000001", "Dhaka"),
            ("donor2", "Donor2@123", "O-", "01700000002", "Chittagong"),
            ("donor3", "Donor3@123", "B+", "01700000003", "Sylhet"),
        ]
        for username, password, group, phone, city in demo_donors:
            user, _ = User.objects.get_or_create(username=username, defaults={"email": f"{username}@example.com"})
            user.set_password(password)
            user.save()
            DonorProfile.objects.get_or_create(
                user=user,
                defaults={
                    "blood_group": group,
                    "phone": phone,
                    "city": city,
                    "available": True,
                },
            )

        # Bank and inventory
        bank, _ = BloodBank.objects.get_or_create(
            name="Central Blood Bank",
            defaults={"address": "123 Main Road", "city": "Dhaka", "phone": "0123456789"},
        )
        for bg in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]:
            inv, _ = BloodInventory.objects.get_or_create(bank=bank, blood_group=bg, defaults={"units_available": 5})

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully."))


