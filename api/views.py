from rest_framework.response import Response
from rest_framework.decorators import api_view
from hospitalapp.models import Location, Hospital
from .serializers import LocationSerializer, HospitalSerializer
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
@api_view(['GET'])
def getLocation(request):
    location = Location.objects.all()
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)

@login_required(login_url='loginpage')
@api_view(['GET'])
def getHospital(request):
    hospital = Hospital.objects.all()
    serializer = HospitalSerializer(hospital, many=True)
    return Response(serializer.data)