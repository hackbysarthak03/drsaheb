from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def SignIn(request):
    roles = UserProfile.ROLE_CHOICES
    if request.method == 'POST':
        role = request.POST.get('role')
        user_username = request.POST.get('user')
        user_psw = request.POST.get('psw')

        
        user = authenticate(username = user_username, password = user_psw)
        if user == None:
            messages.error(request, 'Invalid Credentials')
            return redirect('/sign-in')
        else:

            userRole = UserProfile.objects.filter(user__username = user_username).first().role

            if userRole != role:
                messages.error(request, 'Invalid Credentials')
                return redirect('/sign-in')
            
            else:
                login(request, user)
                return redirect('/')
        
    return render(request, 'SignIn.html', {
        'roles':roles
    })

def Register(request):

    roles = UserProfile.ROLE_CHOICES

    if request.method == 'POST':
        email = request.POST.get('user')
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        psw = request.POST.get('psw')
        cpsw = request.POST.get('cpsw')
        role = request.POST.get('role')

        

        if(len(psw) != len(cpsw)) and psw != cpsw:
            messages.error(request, 'Passwords do not match!')
            return redirect('/signin')

        try:
            user = User.objects.create(
                username = email.split('@')[0],
                email = email,
                first_name = f_name,                
                last_name = l_name
            )
            
            user.set_password(psw)

            user.save()
            userProfile = UserProfile(user = user, role = role)
            userProfile.save()
            messages.success(request, 'Account Created Sucessfully ✅')
        except:
            messages.error(request, 'Account already exist with the Email')
            return redirect('/register')


    return render(request, 'Register.html', {
        'roles':roles
    })