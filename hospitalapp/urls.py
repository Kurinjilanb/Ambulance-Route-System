from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.loginpage, name='loginpage'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('create/', views.hospital_create, name='hospital_create'),
    path('hospital_list/', views.hospital_list, name='hospital_list'),
    path('driver/',views. driver_page, name='driver_page'),
    path('hospital/<int:pk>/update/', views.update_hospital, name='update_hospital'),
    path('hospital/<int:pk>/delete/', views.delete_hospital, name='delete_hospital'),
    path('navigate/', views.navigate_to_destination, name='navigate_to_destination'),
    path('add_location/', views.add_location, name='add_location'),
    path('location_list/', views.location_list, name='location_list'),
    path('', include('api.urls')),
]