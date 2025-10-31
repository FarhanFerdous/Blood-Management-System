from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BloodRequest, Donation
from donors.models import DonorProfile
from banks.models import BloodBank
from django.core.paginator import Paginator


@login_required
def request_create(request):
    if request.method == 'POST':
        bg = request.POST.get('blood_group')
        units = int(request.POST.get('units') or 1)
        reason = request.POST.get('reason') or ''
        if bg not in ["A+","A-","B+","B-","AB+","AB-","O+","O-"]:
            messages.error(request, 'Invalid blood group.')
            return redirect('donations:request_create')
        BloodRequest.objects.create(requester=request.user, blood_group=bg, units=units, reason=reason)
        messages.success(request, 'Request submitted successfully.')
        return redirect('donations:request_list')
    blood_groups = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
    return render(request, 'donations/request_create.html', {"blood_groups": blood_groups})


@login_required
def request_list(request):
    qs = BloodRequest.objects.filter(requester=request.user).order_by('-created_at')
    page = request.GET.get('page')
    requests_page = Paginator(qs, 10).get_page(page)
    return render(request, 'donations/request_list.html', {"requests": requests_page})


@login_required
def donation_history(request):
    profile = DonorProfile.objects.filter(user=request.user).first()
    qs = Donation.objects.filter(donor=profile).select_related('bank').order_by('-created_at') if profile else []
    page = request.GET.get('page')
    donations_page = Paginator(qs, 10).get_page(page) if hasattr(qs, 'model') else []
    return render(request, 'donations/donation_history.html', {"donations": donations_page})

# Create your views here.
