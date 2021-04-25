from django.urls import path
from . import views

app_name = 'supadmin'
urlpatterns = [
    path('', views.main_dashboard, name="admin_home"),
    # path('company', views.company.as_view(), name="company_list"),
    path('company', views.company, name="company_list"),
    path('company/<int:pk>', views.company_view, name="company_profile")
]
