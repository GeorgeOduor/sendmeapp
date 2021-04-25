from django.urls import path
from . import views

# Create your tests here.
app_name = "administrator"

urlpatterns = [
    path('', views.admin_home, name="home"),
    path('vehicle/<int:pk>', views.vehicle_view, name="vehicle"),
    path('vehicle/<int:pk>/delete', views.vehicle_delete.as_view(), name="delete"),
    path('driver/<int:pk>', views.driver_profile, name="driver"),
    path('driver/<int:pk>/driver_delete', views.driver_delete.as_view(), name="driver_delete"),
    # reports
    path('reports/', views.reports_landing, name="reports"),
]
