from django.views.generic import CreateView
from .services import distance, premium, path_to_map
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from .models import Journey, Vehicle, PremiumRate
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .forms import journery_init
from datetime import datetime
from django.utils import timezone
# Create your views here.
def index(request):
    current_user = request.user
    form = journery_init()
    # kdl
    journeyStatus = Journey.objects.filter(JourneyStatus=True, Driver=current_user.id).exists()
    print(journeyStatus)
    submitbutton = 5
    context = {
        "journeyStatus": journeyStatus,
        "form": form
    }
    return render(request, "driver/index.html", context)

# class register(CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/signup____.html'
#     success_url = 'home'

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
            premimum = premium(dist=dist, carValue= vehicle_value, rate=vehicle_stats.YearlyRate)
            journeystat = Journey(From=data['From'], To=data['To'], Distance=dist, Driver_id=current_user.id,
                                  Vehicle_id=vehicles_id, JourneyStatus=1,premium = premimum)
            journeystat.save()
            # print(current_user.id)
            journeystat = Journey.objects.filter(JourneyStatus=True, Driver=current_user.id)
            pathtomap = path_to_map(From=data['From'],To= data['To'])
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
        # print(JourneyStatistics)
    except:
        JourneyStatistics = False

    context = {
        "JourneyStat": JourneyStatistics,
        "pathtomap" : pathtomap
    }
    return render(request, "driver/currentjourney.html", context)

def directions(request):
    context = {
        "webpage": 'https://www.google.com/maps/dir///'
    }
    return render(request, "driver/directions.html", context)

def trip(request):
    current_user = request.user
    # trip_info = Journey.objects.all()
    # currentjourney
    JourneyStat = Journey.objects.filter(JourneyStatus=True, Driver=current_user.id).latest('StartTime')
    # close journey
    Journey(id=JourneyStat.id, EndTime=datetime.now(), Distance=JourneyStat.Distance, Driver_id=current_user.id,
            Vehicle_id=JourneyStat.Vehicle, JourneyStatus=False, premium = JourneyStat.premium,
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

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("driver/index.html")
#     else:
#         form = UserCreationForm()
#         args = {'form':form}
#         return render(request,"driver/signup.html",args)