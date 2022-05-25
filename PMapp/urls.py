from django.urls import path
from . import views

app_name = 'PMapp'

urlpatterns = [
    path('', views.RaceInfo, name='RaceInfo'),
]
