from django import forms
from .models import DonorProfile


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = ["blood_group", "phone", "city", "available", "photo", "last_donated_at"]
        widgets = {
            "last_donated_at": forms.DateInput(attrs={"type": "date"}),
        }


