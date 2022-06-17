from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Surname = models.CharField(max_length=120, null=True)
    FirstName = models.CharField(max_length=120, null=True)
    LastName = models.CharField(max_length=120, null=True)
    NationalID = models.CharField(max_length=20, null=True)
    Gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    YearsofExp = models.IntegerField(null=True)
    company = models.ForeignKey('CompanyProfile', on_delete=models.SET_NULL, null=True, blank=True)
    Role = models.CharField(max_length=10, choices=[
        ('Admin', 'Administartor'),
        ('Driver', 'Driver'),
    ], null=True)
    ProfilePic = models.ImageField(upload_to="ProilePics/", blank=True, null=True)

    # def __str__(self):
    #     return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Vehicle(models.Model):
    VehicleID = models.CharField(max_length=120, null=False)
    VehicleCapacity = models.IntegerField()
    ChasisNo = models.CharField(null=False, max_length=20)
    YearofMan = models.IntegerField(null=False)
    EngineNo = models.CharField(null=False, max_length=12)
    VahicleValue = models.DecimalField(decimal_places=2, null=False, max_digits=27)
    VehicleCapacity = models.IntegerField()
    availability = models.BooleanField(default=False)
    company = models.ForeignKey('CompanyProfile', on_delete=models.CASCADE, null=True, blank=True)
    tlb_licence = models.CharField(null=True, max_length=12)
    tlb_licence_exp_date = models.DateField(null=True)

    def __str__(self):
        return self.VehicleID


class Journey(models.Model):
    From = models.CharField(max_length=120, null=False)
    To = models.CharField(max_length=120, null=False)
    Distance = models.DecimalField(decimal_places=2, max_digits=12)
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    Driver = models.ForeignKey(User, on_delete=models.CASCADE)
    JourneyStatus = models.BooleanField(blank=False, null=False)
    # Passengers = models.IntegerField(blank=False, null=False)
    StartTime = models.DateTimeField(auto_now=True)
    EndTime = models.DateTimeField(auto_now=False, null=True, blank=True)
    premium = models.DecimalField(decimal_places=2, max_digits=12, null=False)
    Duration = models.IntegerField(null=True)

    def __str__(self):
        return "From " + self.From + " to " + self.To


class PremiumRate(models.Model):
    YearlyRate = models.DecimalField(decimal_places=2, null=False, max_digits=3)
    DistRate = models.DecimalField(decimal_places=2, null=False, max_digits=12)
    Supervisor = models.ForeignKey(User, on_delete=models.CASCADE)


class CompanyProfile(models.Model):
    registration_number = models.CharField(null=False, max_length=200)
    registration_name = models.CharField(null=False, max_length=200)
    company_logo = models.ImageField(upload_to="ProilePics/", blank=True, null=True)

    def __str__(self):
        return self.registration_name
