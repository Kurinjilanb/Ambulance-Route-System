import googlemaps
from django.shortcuts import render,redirect
from .models import Hospital
from routeapp.forms import HospitalForm

def map_view(request):
    gmaps = googlemaps.Client(key='AIzaSyA3-WBgrAIgrvGK3YX7nITbUX3UsllpR5Q')
    geocode_result = gmaps.geocode('Empire State Building')
    location = geocode_result[0]['geometry']['location']
    context = {
        'lat': location['lat'],
        'lng': location['lng'],
    }
    return render(request, 'map/map.html', context)

def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_map')
    else:
        form = HospitalForm()
    return render(request, 'map/add_hospital.html', {'form': form})


def hospital_map(request):
    hospitals = Hospital.objects.all()
    context = {'hospitals': hospitals}
    return render(request, 'map/hospital_map.html', context)

