from django.shortcuts import render, redirect, get_object_or_404
from homepagedb.models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from department.models import *
from account.models import UserProfile
from doctor.models import DoctorProfile
from patient.models import PatientProfile
from bookings.models import Booking

def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'AboutUs.html')

def bookings(request):
    user = UserProfile.objects.filter(user__username = request.user).first()
    role = user.role

    if role == 'patient':
        patient = PatientProfile.objects.filter(user__username = request.user).first()
        books = Booking.objects.filter(patient_profile = patient).order_by('-booked_on')
        
        return render(request, 'PatientBooking.html', {
            'userProfile':user,
            'bookings':books
        })
    
    else:
        doctor = DoctorProfile.objects.filter(user__username = request.user).first()
        books = Booking.objects.filter(doctor_profile = doctor).order_by('-booked_on')
        
        return render(request, 'DoctorBooking.html', {
            'userProfile':user,
            'bookings':books
        })


def signOut(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/sign-in/')
def Services(request):
    data = Department.objects.all()

    return render(request, 'Services.html', {
        'departments':data
    })

@login_required(login_url='/sign-in/')
def depart(request, slug):
    data = Department.objects.filter(slug = slug).first()
    doctors = DoctorProfile.objects.filter(department = data)
    
    return render(request, 'Departments.html', {
        'data':data,
        'doctors':doctors
    })


@login_required(login_url='/sign-in/')
def updateProfile(request, user_name):
    userProfile = UserProfile.objects.filter(user__username = user_name).first()
    userRole = userProfile.role

    if request.method == 'POST':
        if 'save-profile' in request.POST:
            if userRole == 'doctor':
                dep = request.POST.get('dept')
                reg_no = request.POST.get('reg_no')
                specialist = request.POST.get('specialist')
                hospital = request.POST.get('hospital')
                hospital_district = request.POST.get('hospital_district')
                hospital_state = request.POST.get('hospital_state')
                fees = request.POST.get('fees')
                bio = request.POST.get('desc')
                
                print(fees)
                # Saving the New Profile
                if not DoctorProfile.objects.filter(user__username = user_name).exists():

                    dep = Department.objects.get(name = dep)
                    data = DoctorProfile.objects.create(
                        user = request.user,
                        department = dep,
                        reg_no = reg_no,
                        specialist = specialist,
                        hospital = hospital,
                        hospital_district = hospital_district,
                        hospital_state = hospital_state,
                        fees = fees,
                        desc = bio,
                    )

                
                    data.save()
                    url = '/profile/' + user_name
                    return redirect(url)
                
                # Updating the Profile
                else:
                    dep = Department.objects.get(name = dep)
                    data = DoctorProfile.objects.filter(user__username = user_name).first()
                    data.department = dep
                    data.reg_no = reg_no
                    data.specialist = specialist
                    data.hospital = hospital
                    data.hospital_district = hospital_district,
                    data.hospital_state = hospital_state,
                    data.fees = fees,
                    data.desc = bio,
                    
                    
                    data.save()
                    url = '/profile/' + user_name
                    return redirect(url)
            else:
                desc = request.POST.get('desc')
                district = request.POST.get('district')
                state = request.POST.get('state')
                healthcard = request.POST.get('healthcard')

                if not PatientProfile.objects.filter(user__username = user_name).exists():
                    data = PatientProfile.objects.create(
                        user = request.user,
                        desc = desc,
                        state = state,
                        district = district,
                        healthCard = healthcard
                    )

                
                    data.save()
                    url = '/profile/' + user_name
                    return redirect(url)
                
                else:
                    data = PatientProfile.objects.filter(user__username = user_name).first()
                    data.desc = desc
                    data.district = district
                    data.state = state
                    data.healthCard = healthcard

                    data.save()
                    url = '/profile/' + user_name
                    return redirect(url)


        elif 'save-avatar' in request.POST:

            img = request.FILES.get('avatar')

            data = UserProfile.objects.filter(user__username = user_name).first()
            data.avatar = img

            data.save()
            
            url = '/profile/' + user_name
            return redirect(url)
        else:
            pass

    dept = Department.objects.all()
    
    if userRole == 'doctor':
    
        data = DoctorProfile.objects.filter(user__username = user_name)

        if data.exists():
            
            return render (request, 'UpdateProfile.html', {
                'doctor':True,
                'users': userProfile,
                'profileExists':True,
                'profile':data.first(),
                'department':dept
            })
        else:
            
            return render(request, 'UpdateProfile.html', {
                'doctor':True,
                'users': userProfile,
                'profileExists':False,
                'department':dept
            })
    
    else:
        data = PatientProfile.objects.filter(user__username = user_name)

        if data.exists():
            
            return render (request, 'UpdateProfile.html', {
                'doctor':False,
                'users': userProfile,
                'profileExists':True,
                'profile':data.first(),
                'department':dept
            })
        else:
            
            return render(request, 'UpdateProfile.html', {
                'doctor':False,
                'users': userProfile,
                'profileExists':False,
                'department':dept
            })


# Profile Definition
@login_required(login_url='/sign-in/')
def profile(request, user_name):
    userProfile = UserProfile.objects.filter(user__username = user_name).first()
    userRole = str(userProfile.role)

    if userRole == 'doctor':
        
        data = DoctorProfile.objects.filter(user__username = user_name)

        if data.exists():

            if request.method == 'POST':
                doc = get_object_or_404(DoctorProfile, user = userProfile.user)
                doc.avail = not doc.avail
                doc.save()

            return render (request, 'MyProfile.html', {
                'doctor':True,
                'users': userProfile,
                'profileExists':True,
                'profile':data.first()
            })
        else:
            
            return render(request, 'MyProfile.html', {
                'doctor':True,
                'users': userProfile,
                'profileExists':False
            })
    
    else:
        
        data = PatientProfile.objects.filter(user__username = user_name)

        if data.exists():
            
            return render (request, 'MyProfile.html', {
                'doctor':False,
                'users': userProfile,
                'profileExists':True,
                'profile':data.first()
            })
        else:
            
            return render(request, 'MyProfile.html', {
                'doctor':False,
                'users': userProfile,
                'profileExists':False
            })


