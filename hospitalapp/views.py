from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import HospitalForm
from .forms import LocationForm, UserForm
from .models import Hospital
from .models import Location
import json
import hospital.settings as settings
from .models import Location, Hospital
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthentication_user, allowed_users



def signup(request):
    """
    signup view function renders the signup.html template
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('hospital_list')
    else:
        form = UserForm()
        context = {'form': form}
        return render(request, 'hospital/signup.html', context)

@unauthentication_user
def loginpage(request):
    """
    loginpage view function renders the login.html template 
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('driver_page')  
    return render(request, 'hospital/loginpage.html')

def logoutpage(request):
    """
    logoutpage view function renders the logout.html template 
    """
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
@allowed_users(allowed_roles='[admin]')
def hospital_create(request):
    """
    hospital_create view function renders the hospital_form.html template 
    """
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'hospital/hospital_form.html', {'form': form})

@login_required(login_url='loginpage')
@allowed_users(allowed_roles='[admin]')
def hospital_list(request):
    """
    hospital_list view function renders the hospital_list.html template 
    """
    hospitals = Hospital.objects.all()
    context = {'hospitals': hospitals}
    return render(request, 'hospital/hospital_list.html', context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles='[admin]')
def hospital_update(request, hospital_id):
    hospital = Hospital.objects.get(id=hospital_id)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'hospital/hospital_form.html', {'form': form})

@login_required(login_url='loginpage')
def driver_page(request):
    """
    driver_page view function renders the driver_page.html template 
    """
    hospitals = Hospital.objects.all()
    context = {'hospitals': hospitals}
    return render(request, 'hospital/driver_page.html', context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles='[admin]')
def update_hospital(request, pk):
    """
    update_hospital view function renders the update_hospital.html template 
    """
    # hospital = Hospital.objects.get(id=hospital_id)
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('driver_page')
    else:
        form = HospitalForm(instance=hospital)
    context = {'form': form}
    return render(request, 'hospital/update_hospital.html', context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles='[admin]')
def delete_hospital(request, pk):
    """
    delete_hospital view function renders the delete_hospital.html template 
    """
    hospital = get_object_or_404(Hospital, pk=pk)
    hospital.delete()
    return redirect('driver_page')

@login_required(login_url='loginpage')
def home(request):
    return render(request, 'hospital/driver.html')

@login_required(login_url='loginpage')
def navigate_to_destination(request):
    """
    navigate_to_destination view function renders the navigate_to_destination.html template 
    """
    url = 'https://www.googleapis.com/geolocation/v1/geolocate'
    params = {'key': settings.GOOGLE_MAP}

    # Send a POST request to the Geolocation API endpoint
    response = requests.post(url, params=params)

    # Parse the JSON response and extract the latitude and longitude coordinates
    result = json.loads(response.text)
    lat = result['location']['lat']
    lng = result['location']['lng']

    # Step 2: Use the Google Maps Directions API to generate turn-by-turn directions

    # Set up the Directions API endpoint and parameters
    url = 'https://maps.googleapis.com/maps/api/directions/json'
    params = {
        'origin': f'{lat},{lng}',
        'destination': 'Bangalore, India',
        'mode': 'driving',
        'key': settings.GOOGLE_MAP
    }

    # Send a GET request to the Directions API endpoint
    response = requests.get(url, params=params)

    # Parse the JSON response and extract the turn-by-turn directions
    result = json.loads(response.text)
    steps = result['routes'][0]['legs'][0]['steps']

    # Step 3: Use a navigation app on the user's mobile device to display the directions

    # Construct the navigation app URL and redirect the user to it
    url = f'https://www.google.com/maps/dir/?api=1&origin={lat},{lng}&destination=Bangalore, India&travelmode=driving'
    return redirect(url)

@login_required(login_url='loginpage')
def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'hospital/add_location.html', {'form': form})

@login_required(login_url='loginpage')
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'hospital/location_list.html', {'locations': locations})