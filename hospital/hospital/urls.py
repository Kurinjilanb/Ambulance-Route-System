from django.urls import path
from hospitalapp.views import hospital_create, hospital_list, driver_page, update_hospital  

urlpatterns = [
    path('hospital/create/', hospital_create, name='hospital_create'),
    path('hospital/', hospital_list, name='hospital_list'),
    path('driver/', driver_page, name='driver_page'),
    path('hospital/<int:pk>/update/', update_hospital, name='update_hospital'),
]
