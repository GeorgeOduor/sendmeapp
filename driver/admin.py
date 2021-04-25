from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Profile, Vehicle, Journey, PremiumRate, CompanyProfile


class Journey_adminview(admin.ModelAdmin):
    list_display = ('id', 'From', 'To', 'Driver_id', 'Vehicle_id', 'StartTime', 'EndTime', 'Duration','JourneyStatus', 'premium')
    list_display_links = ('From',)
    search_fields = ('From',)
    list_filter = ('JourneyStatus', 'Vehicle_id')


class driver_adminview(admin.ModelAdmin):
    list_display = ('user', 'Surname', 'LastName', 'FirstName', 'NationalID', 'Gender', 'YearsofExp','Role', 'company','ProfilePic',)
    list_display_links = ('user',)
    search_fields = ('NationalID',)
    list_filter = ('Gender',)


class CompanyProfile_adminView(admin.ModelAdmin):
    list_display = ('registration_number', 'registration_name')
    list_display_links = ('registration_number',)
    search_fields = ('registration_number',)
    list_filter = ('registration_name',)


admin.site.register(Profile, driver_adminview)
admin.site.register(Vehicle, ImportExportModelAdmin)
admin.site.register(Journey, Journey_adminview)
admin.site.register(PremiumRate)
admin.site.register(CompanyProfile, CompanyProfile_adminView)
