from django.shortcuts import render
import random
from django.contrib.auth.models import User
from doctor.models import DoctorProfile
from account.models import UserProfile

# Create your views here.

def home(request):
    userProfile = UserProfile.objects.filter(user__username = request.user).first()

    if userProfile.role == 'doctor':
        current_user = User.objects.filter(username = request.user).first()
        roomID = str(request.user) + str(random.randint(1, 10000))

        doctor = DoctorProfile.objects.filter(user__username = request.user).first()

        doctor.room_id = roomID
        doctor.save()
        
        return render(request, 'VideoCall.html', {
            'room_id':doctor.room_id,
            'user':current_user
        })
    

    return render(request, 'VideoCall.html')