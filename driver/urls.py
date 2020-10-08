from django.urls import path
from . import views
app_name = 'driver'
urlpatterns = [
    path('', views.index, name="home"),
    # path('login', views.loginPage, name="login"),
    # path('logout/', views.logout, name="logout"),
    # path('signup/', views.register, name="signup"),
    path('currentjourney/', views.currentjourney, name="currentjourney"),
    path('directions/', views.directions, name="directions"),
    path('trip/', views.trip, name="trip"),
    path('error/', views.error, name="error"),
]
