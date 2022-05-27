from django.urls import path
from . import views

app_name = 'PMapp'

urlpatterns = [
    path('', views.RaceInfo, name='RaceInfo'),
    path('Race_list/', views.Race_list.as_view(), name='Race_list'),
    path('Race_detail/<int:pk>/', views.RaceDetail.as_view(), name='Race_detail'),
    path('Race_delete/<int:pk>/', views.RaceDelete.as_view(), name='Race_delete'),
    path('Race_update/<int:pk>/', views.RaceUpdate.as_view(), name='Race_update'),
    path('MenuInfo/', views.MenuInfo, name='MenuInfo'),
    path('Menu_list/', views.Menu_list.as_view(), name='Menu_list'),
    path('Menu_detail/<int:pk>/', views.MenuDetail.as_view(), name='Menu_detail'),
    path('Menu_delete/<int:pk>/', views.MenuDelete.as_view(), name='Menu_delete'),
    path('Menu_update/<int:pk>/', views.MenuUpdate.as_view(), name='Menu_update'),
    
    path('Calcurate_Cal/', views.Calcurate_Cal, name='Calcurate_Cal'),
    
]
