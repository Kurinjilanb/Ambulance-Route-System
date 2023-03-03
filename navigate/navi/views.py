import requests
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def navigate_to_destination(request):
    # Step 1: Use the Google Maps Geolocation API to get the user's current location
    
    # Set up the Geolocation API endpoint and parameters
    url = 'https://www.googleapis.com/geolocation/v1/geolocate'
    params = {'key': 'AIzaSyA3-WBgrAIgrvGK3YX7nITbUX3UsllpR5Q'}
    
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
        'key': 'AIzaSyA3-WBgrAIgrvGK3YX7nITbUX3UsllpR5Q'
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
