from django.shortcuts import render, redirect
from patient.models import PatientProfile
from doctor.models import DoctorProfile
from .models import Booking
from datetime import datetime
import random


# Create your views here.

def bookDoctor(request, slug):
    current_user = request.user
    patient = PatientProfile.objects.filter(user__username = current_user).first()
    doctor = DoctorProfile.objects.filter(user__username = slug).first()
    
    Booking.objects.create(
        patient_profile = patient,
        doctor_profile = doctor
    )

    return redirect('/my-bookings/')

def invite(request, id):
    book = Booking.objects.filter(id = id).first()
    book.status = 1
    book.save()

    return redirect('/my-bookings/')

def checkUp(request, id):
    if request.method == 'POST':
        
        book = Booking.objects.filter(id = id).first()
        book.prescription = request.POST.get('prescribe')
        book.status = 2
        book.save()
        
        return redirect('/my-bookings/')
    
def generate_pdf(request, id):
    book = Booking.objects.filter(id = id).first()

    if not book.prescribed_date:
        book.prescribed_date = datetime.now()
        book.pr_no = str(random.randint(1, 1000)) + '-' + str(str(datetime.now().time()).replace(':','').replace('.', '')) + '-' + 'drsaheb'
        book.save()

    return render(request, 'pdf_template.html', {
        'booking':book
    })
        