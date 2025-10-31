from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DonorProfile
from .forms import DonorProfileForm
from django.core.paginator import Paginator


@login_required
def profile_edit(request):
    profile, _ = DonorProfile.objects.get_or_create(user=request.user, defaults={"blood_group": "A+", "phone": "", "city": ""})
    if request.method == 'POST':
        form = DonorProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('donors:profile_edit')
    else:
        form = DonorProfileForm(instance=profile)
    return render(request, 'donors/profile_edit.html', {"form": form, "profile": profile})

def donor_search(request):
    qs = DonorProfile.objects.select_related('user').filter(available=True)
    blood_group = request.GET.get('blood_group') or ''
    city = request.GET.get('city') or ''
    if blood_group:
        qs = qs.filter(blood_group=blood_group)
    if city:
        qs = qs.filter(city__icontains=city)
    paginator = Paginator(qs.order_by('city', 'user__username'), 10)
    page = request.GET.get('page')
    donors = paginator.get_page(page)
    return render(request, 'donors/search.html', {"donors": donors, "blood_group": blood_group, "city": city})


# Create your views here.
