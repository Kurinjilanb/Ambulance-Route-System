from django.shortcuts import render

import requests

def find_directions(request):
    origin = request.GET.get('origin', '')
    destination = request.GET.get('destination', '')
    steps = []
    
    if origin and destination:
        steps = get_directions(origin, destination)
        

    return render(request, 'find_directions.html', {'steps': steps})



def get_directions(origin, destination):
    API_KEY = 'AIzaSyA3-WBgrAIgrvGK3YX7nITbUX3UsllpR5Q'
    url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_KEY}'

    response = requests.get(url)
    data = response.json()
   

    return data['routes'][0]['legs'][0]['steps']

    