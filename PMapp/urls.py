from django.urls import path
from . import views

app_name = 'PMapp'

urlpatterns = [
    path('', views.RaceInfo, name='RaceInfo'),
    path('Race_list/', views.Race_list.as_view(), name='Race_list'),
    path('Race_detail/<int:pk>/', views.RaceDetail.as_view(), name='Race_detail'),
    path('Race_delete/<int:pk>/', views.RaceDelete.as_view(), name='Race_delete'),
    path('Race_update/<int:pk>/', views.RaceUpdate.as_view(), name='Race_update'),
]
