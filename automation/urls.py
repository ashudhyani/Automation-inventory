from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/login-automation/', views.login_automation, name='login_automation'),
]
