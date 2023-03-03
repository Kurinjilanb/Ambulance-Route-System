from django.shortcuts import render, redirect,get_object_or_404
from .forms import HospitalForm
from .models import Hospital

def hospital_create(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'hospital_form.html', {'form': form})

def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital_list.html', {'hospitals': hospitals})

def hospital_update(request, hospital_id):
    hospital = Hospital.objects.get(id=hospital_id)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'hospital_form.html', {'form': form})

def driver_page(request):
    hospitals = Hospital.objects.all()
    context = {'hospitals': hospitals}
    return render(request, 'driver_page.html', context)

def update_hospital(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('driver_page')
    else:
        form = HospitalForm(instance=hospital)
    context = {'form': form}
    return render(request, 'update_hospital.html', context)