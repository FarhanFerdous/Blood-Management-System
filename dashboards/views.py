from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from donors.models import DonorProfile
from donations.models import BloodRequest, Donation
from banks.models import BloodBank, BloodInventory


def home_view(request):
    return render(request, 'home.html')


@login_required
def donor_dashboard(request):
    profile = DonorProfile.objects.filter(user=request.user).first()
    total_donations = Donation.objects.filter(donor=profile).count() if profile else 0
    context = {
        'profile': profile,
        'total_donations': total_donations,
    }
    return render(request, 'dashboards/donor_dashboard.html', context)


def is_admin_user(user: User) -> bool:
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(is_admin_user)
def admin_dashboard(request):
    total_donors = DonorProfile.objects.count()
    pending_requests = BloodRequest.objects.filter(status='pending').count()
    # Sum available units across inventory
    from django.db.models import Sum
    total_units = BloodInventory.objects.aggregate(total=Sum('units_available'))['total'] or 0
    context = {
        'total_donors': total_donors,
        'pending_requests': pending_requests,
        'total_units': total_units,
    }
    return render(request, 'dashboards/admin_dashboard.html', context)


def demo_walkthrough(request):
    return render(request, 'dashboards/demo.html')


def _get_demo_donor() -> User:
    try:
        return User.objects.get(username='donor1')
    except User.DoesNotExist:
        return None


def demo_create_request(request):
    demo_user = _get_demo_donor()
    if not demo_user:
        messages.error(request, 'Demo donor not found. Please run seed script again.')
        return redirect('dashboards:demo_walkthrough')
    BloodRequest.objects.create(requester=demo_user, blood_group='A+', units=2, reason='Demo need')
    messages.success(request, 'Created a demo blood request (A+ x2) for donor1.')
    return redirect('dashboards:demo_walkthrough')


def demo_approve_request(request):
    req = BloodRequest.objects.filter(status='pending').order_by('created_at').first()
    if not req:
        messages.info(request, 'No pending requests to approve.')
        return redirect('dashboards:demo_walkthrough')
    # Reduce inventory if available
    bank = BloodBank.objects.first()
    inv = None
    if bank:
        inv = BloodInventory.objects.filter(bank=bank, blood_group=req.blood_group).first()
    if inv and inv.units_available >= req.units:
        inv.units_available -= req.units
        inv.save()
        req.status = 'approved'
        req.save()
        messages.success(request, f'Approved request {req.blood_group} x{req.units} and updated inventory at {bank.name}.')
    else:
        req.status = 'rejected'
        req.save()
        messages.warning(request, 'Insufficient inventory. Request marked as rejected.')
    return redirect('dashboards:demo_walkthrough')


def demo_create_donation(request):
    demo_user = _get_demo_donor()
    if not demo_user:
        messages.error(request, 'Demo donor not found. Please run seed script again.')
        return redirect('dashboards:demo_walkthrough')
    profile = DonorProfile.objects.filter(user=demo_user).first()
    bank = BloodBank.objects.first()
    if not (profile and bank):
        messages.error(request, 'Missing donor profile or bank for demo donation.')
        return redirect('dashboards:demo_walkthrough')
    Donation.objects.create(donor=profile, bank=bank, units=1, approved=True)
    inv, _ = BloodInventory.objects.get_or_create(bank=bank, blood_group=profile.blood_group, defaults={'units_available': 0})
    inv.units_available += 1
    inv.save()
    messages.success(request, f'Created a demo donation (+1 unit {profile.blood_group}) at {bank.name}.')
    return redirect('dashboards:demo_walkthrough')

# Create your views here.
