from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from driver.models import Profile, Vehicle, Journey, CompanyProfile


# Create your views here.


@login_required
def admin_home(request):
    current_user = request.user
    profiles = Profile.objects
    group = profiles.filter(user=current_user).values('Role')
    # company
    company_id = profiles.filter(user=current_user).values('company')[0]['company']
    company_name = CompanyProfile.objects.filter(id=company_id).values('registration_name')[0]['registration_name']

    # vehicles
    vehicles = Vehicle.objects.filter(company_id=company_id)
    # drivers
    drivers = profiles.filter(Role="Driver", company_id=company_id)
    journey = Journey.objects.prefetch_related('Vehicle').filter(Vehicle__company_id=company_id)
    counts = journey.values('StartTime') \
        .annotate(StartDate=TruncDate('StartTime')) \
        .order_by('StartDate') \
        .values('StartDate') \
        .annotate(**{'count': Count('StartTime')})

    dataset = [i for i in counts.values_list('count', flat=True)]
    dates = [dt.strftime('%d-%m-%Y') for dt in counts.values_list('StartDate', flat=True)]

    # vals =
    # print(vals)
    context = {
        'valueboxes': {
            'vehicle_count': vehicles.count(),
            'drivers': drivers.count(),
            'on_transit': journey.filter(JourneyStatus=True).count(),
            'total_journeys': journey.count()
        },
        'chart_data': {
            'labels': dates[-5:],
            'dataset': dataset[-5:]
        },
        'drivers': drivers,
        'vehicles2': vehicles,
        'user': current_user,
        'company_name': company_name
    }

    if group.values()[0]['Role'] == "Driver":
        return redirect("/")
    else:
        return render(request, "administrator/dashboard.html", context)


@login_required
def vehicle_view(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    milage = Journey.objects.filter(Vehicle_id=pk)
    # print(milage.values())

    context = {
        'vehicle_details': {
            'RegistrationNumber': vehicle.VehicleID,
            'ChassisNumber': vehicle.ChasisNo,
            'EngineNumber': vehicle.EngineNo,
            'YearofManufacture': vehicle.YearofMan,
            'VehicleValue': vehicle.VahicleValue,
            'VehicleCapacity': vehicle.VehicleCapacity,
            'VehicleAvailability': vehicle.availability,
            'TLBLicence': vehicle.tlb_licence,
            'TLBExpirationDate': vehicle.tlb_licence_exp_date,
            'vehicle_id': vehicle.id
        }, 'milage': milage
    }

    return render(request, "administrator/vehicle.html", context)


class vehicle_delete(LoginRequiredMixin, generic.DeleteView):
    template_name = 'administrator/delete_vehicle.html'
    queryset = Vehicle.objects.all()

    def get_success_url(self):
        return reverse("administrator:home")


@login_required
def driver_profile(request, pk):
    profiles = Profile.objects.get(user_id=pk)
    # stats = profiles.aggregate(sum = Sum('Distance'))
    journey = Journey.objects.filter(Driver_id=pk)
    print(profiles.id)
    context = {
        'driver_details': profiles,
        'journey_stats': journey.aggregate(timetaken=Sum('Duration'),
                                           distance_trav=Sum('Distance'),
                                           TripsDone=Count('From')),
        'trips': journey
    }
    return render(request, "administrator/driver_profile.html", context)


class driver_delete(LoginRequiredMixin, generic.DeleteView):
    template_name = 'administrator/delete_driver.html'
    queryset = Profile.objects.all()

    def get_success_url(self):
        return reverse("administrator:home")


@login_required
def reports_landing(request):
    template_name = 'administrator/tabs_landing.html'
    profiles = Profile.objects
    current_user = request.user
    # company
    company_id = profiles.filter(user=current_user).values('company')[0]['company']
    print(company_id)
    journey = Journey.objects.prefetch_related('Vehicle'). \
        filter(Vehicle__company_id = company_id). \
        values(
        "From", "To", "Driver", "StartTime", "Driver_id", "EndTime", "Distance","Duration", "premium"
    )
    context = {
        'journey':journey
    }
    # print(journey)
    return render(request, template_name,context)
