from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import driver, Vehicle, Journey, PremiumRate


class Journey_adminview(admin.ModelAdmin):
    list_display = ('id', 'From', 'To', 'Driver_id', 'Vehicle_id', 'StartTime', 'EndTime', 'JourneyStatus', 'premium')
    list_display_links = ('From',)
    search_fields = ('From',)
    list_filter = ('JourneyStatus', 'Vehicle_id')

class driver_adminview(admin.ModelAdmin):
    list_display = ('Surname', 'LastName', 'FirstName', 'NationalID', 'Gender', 'YearsofExp', 'ProfilePic',)
    list_display_links = ('Surname',)
    search_fields = ('NationalID',)
    list_filter = ('Gender',)


admin.site.register(driver,driver_adminview)
admin.site.register(Vehicle, ImportExportModelAdmin)
admin.site.register(Journey, Journey_adminview)
admin.site.register(PremiumRate)
