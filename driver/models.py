from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class driver(models.Model):
    Surname = models.CharField(max_length=120, null=False)
    FirstName = models.CharField(max_length=120, null=True)
    LastName = models.CharField(max_length=120, null=True)
    NationalID = models.CharField(max_length=20, null=False)
    Gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    YearsofExp = models.IntegerField()
    ProfilePic = models.ImageField(upload_to="ProilePics/", blank=True, null=True)

    def __str__(self):
        return self.NationalID


class Vehicle(models.Model):
    VehicleID = models.CharField(max_length=120, null=False)
    VehicleCapacity = models.IntegerField()
    ChasisNo = models.CharField(null=False,max_length=20)
    YearofMan = models.IntegerField(null=False)
    EngineNo = models.CharField(null=False,max_length=12)
    VahicleValue = models.DecimalField(decimal_places=2,null=False,max_digits=27)
    VehicleCapacity = models.IntegerField()
    Driver = models.ForeignKey(driver, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.VehicleID


class Journey(models.Model):
    From = models.CharField(max_length=120, null=False)
    To = models.CharField(max_length=120, null=False)
    Distance = models.DecimalField(decimal_places=2, max_digits=12)
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Driver = models.ForeignKey(driver, on_delete=models.CASCADE)
    JourneyStatus = models.BooleanField(blank=False, null=False)
    # Passengers = models.IntegerField(blank=False, null=False)
    StartTime = models.DateTimeField(auto_now=True)
    EndTime = models.DateTimeField(auto_now=False, null=True, blank=True)
    premium = models.DecimalField(decimal_places=2,max_digits=12,null=False)

    def __str__(self):
        return "From " + self.From + " to " + self.To

class PremiumRate(models.Model):
    YearlyRate = models.DecimalField(decimal_places=2,null=False,max_digits=3)
    DistRate = models.DecimalField(decimal_places=2,null=False,max_digits=12)
    Supervisor = models.ForeignKey(User,on_delete=models.CASCADE)