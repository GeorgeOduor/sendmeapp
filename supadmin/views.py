from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render
from django.views.generic import ListView
from driver.models import Vehicle, CompanyProfile, Profile, Journey
from .tables import SimpleTable


# Create your views here.

def main_dashboard(request):
    vehicles = Vehicle.objects.all()
    companies = CompanyProfile.objects.all()
    trips = Journey.objects.all()
    journeys = trips.values('StartTime') \
        .annotate(StartDate=TruncDate('StartTime')) \
        .order_by('StartDate') \
        .values('StartDate') \
        .annotate(**{'count': Count('StartTime')})

    print(journeys)
    drivers = Profile.objects.filter(Role='Driver')

    context = {
        'cards': {
            'v': vehicles.count(),
            'c': companies.count(),
            'd': drivers.count(),
            't': trips.count(),
        },
        'dates': [dt.strftime('%d-%m-%Y') for dt in journeys.values_list('StartDate', flat=True)],
        "counts": [i for i in journeys.values_list('count', flat=True)]
    }
    return render(request, "supadmin/dashboard.html", context)


def company(request):
    comp = CompanyProfile.objects.all()
    table = SimpleTable(comp)
    context = {
        'comp': comp,
        'table': table
    }
    return render(request, "supadmin/company_listing.html", context)


def company_view(request, pk):
    comp = CompanyProfile.objects.get(pk=pk)
    context = {
        'company':comp
    }
    return render(request, "supadmin/company_one.html",context)
