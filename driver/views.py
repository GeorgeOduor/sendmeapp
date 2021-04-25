from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .services import distance, premium, path_to_map
from .forms import LoginForm, SignUpForm, profile_update
from .models import Journey, Vehicle, PremiumRate, Profile
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import journery_init
from datetime import datetime

from django.utils import timezone


# Create your views here.
def index(request):
    signup = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/welcome")
    else:
        form = SignUpForm()

    current_user = request.user
    form = journery_init()
    # kdl

    submitbutton = 5
    context = {
        "journeyStatus": Journey.objects.filter(JourneyStatus=True, Driver=current_user.id).exists(),
        "form": form,
        'form2': signup
    }
    return render(request, "driver/index.html", context)


def currentjourney(request):
    current_user = request.user
    form = journery_init(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        dist = distance(From=data['From'], To=data['To'])
        vehicle_stats = PremiumRate.objects.last()
        if dist == None:
            return redirect("/error")
        else:
            # calculatePremium

            journeystat = Journey.objects.filter(JourneyStatus=True, Driver=current_user.id, Vehicle=data['Vehicle'])
            vehicles_id, vehicle_reg, vehicle_value = \
                Vehicle.objects.filter(VehicleID=data['Vehicle']).values_list('id', 'VehicleID', 'VahicleValue')[0]
            premimum = premium(dist=dist, carValue=vehicle_value, rate=vehicle_stats.YearlyRate)
            df = (data['From'],data['To'], dist, current_user.id,vehicles_id, 1,premimum)
            journeystat = Journey(From=data['From'], To=data['To'], Distance=dist, Driver_id=current_user.id,
                                  Vehicle_id=vehicles_id, JourneyStatus=1, premium=premimum)
            journeystat.save()
            journeystat = Journey.objects.filter(JourneyStatus=True, Driver=current_user.id)

            pathtomap = path_to_map(From=data['From'], To=data['To'])
    else:
        journeystat = Journey.objects.filter(JourneyStatus=True, Driver=current_user.id)
        From = list(journeystat.values_list('From', flat=True))[0]
        To = list(journeystat.values_list('To', flat=True))[0]
        pathtomap = path_to_map(From, To)

    try:
        JourneyStatistics = {
            "From": list(journeystat.values_list('From', flat=True))[0],
            "To": list(journeystat.values_list('To', flat=True))[0],
            "Distance (km)": list(journeystat.values_list('Distance', flat=True))[0]
        }

    except:
        JourneyStatistics = False

    context = {
        "JourneyStat": JourneyStatistics,
        "pathtomap": pathtomap
    }
    return render(request, "driver/currentjourney.html", context)


def directions(request):
    context = {
        "webpage": 'https://www.google.com/maps/dir///'
    }
    return render(request, "driver/directions.html", context)


def trip(request):
    current_user = request.user
    # currentjourney
    JourneyStat = Journey.objects.filter(
        JourneyStatus=True,
        Driver=current_user.id).latest('StartTime')
    endjourney = datetime.now(timezone.utc) - JourneyStat.StartTime

    # close journey
    Journey(id=JourneyStat.id, EndTime=datetime.now(),
            Distance=JourneyStat.Distance,
            Driver_id=current_user.id,
            Vehicle_id=JourneyStat.Vehicle,
            JourneyStatus=False,
            Duration = round(endjourney.total_seconds()/3600),
            premium=JourneyStat.premium,
            From=JourneyStat.From, To=JourneyStat.To).save()
    context = {
        "webpage": '' + "5"
    }
    return render(request, "driver/trip_stat.html", context)


def error(request):
    context = {
        'e': "Mmmh,one of the towns you've entered is not correct.Please check and try again"
    }
    return render(request, "driver/error.html", context)

@login_required
def landing(request):
    current_user = request.user
    form1 = profile_update(request.POST)
    if form1.is_valid():
        data = form1.cleaned_data
        Profile.objects.filter(user=current_user).update(
                Surname=data['Surname'],
                FirstName=data['FirstName'],
                LastName=data['LastName'],
                NationalID=data['NationalID'],
                Gender=data['Gender'],
                company=data['company'],
                Role=data['Role'],
        )
        if data['Role'] == "Driver":
            # # assign group
            # user = request.user
            # group = Group.objects.get(name='Drivers')
            # user.groups.add(group)
            return redirect('/')
        else:
            # assign group
            # user = request.user
            # group = Group.objects.get(name='Administrator')
            # user.groups.add(group)
            return redirect("/agent")
    else:
        print('form1')
    context = {
        'user': current_user,
        'form': form1,
    }
    return render(request, "driver/landing.html", context)
