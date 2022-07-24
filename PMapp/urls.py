from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'PMapp'

urlpatterns = [
    path('RaceInfo/', views.RaceInfo, name='RaceInfo'),
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

    path('', views.Home.as_view(), name='Home'),
    path('Login/', views.Login.as_view(), name='Login'), #for login
    path('auth/', include('social_django.urls', namespace='social')), 
    path('Logout/', views.Logout.as_view(), name='Logout'), # for logout
    path('My_page/<int:pk>/', views.MyPage.as_view(), name='My_page'), # my info
    path('Signup/', views.Signup.as_view(), name='Signup'), # sign up
    path('Signup_done/', views.SignupDone.as_view(), name='Signup_done'), # sign up end
    path('User_update/<int:pk>', views.UserUpdate.as_view(), name='User_update'), # update user
    path('Password_change/', views.PasswordChange.as_view(), name='Password_change'), # pass change
    path('Password_change_done/', views.PasswordChangeDone.as_view(), name='Password_change_done'), # pass change cmp
    
]
