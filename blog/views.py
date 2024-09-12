from django.shortcuts import render, redirect
from account.models import UserProfile
from doctor.models import DoctorProfile
from department.models import Department
from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
def has_common_elements(list1, list2):
    return bool(set(list1) & set(list2))

@login_required(login_url='/sign-in/')
def Blogs(request):
    dep = Department.objects.all()
    blogs = Blog.objects.all()
    

    if request.method == 'POST':
        if 'apply-filter' in request.POST:
            newList = []
            selected_filter = request.POST.getlist('category')
            for blog in blogs:
                blogList = list(blog.category)
                if has_common_elements(selected_filter, blogList):
                    newList.append(blog)

            if selected_filter:
                data = {
                'department':dep,
                'filters':selected_filter,
                'blogs':newList
                }
            
            else:
                data = {
                'department':dep,
                'filters':selected_filter,
                'blogs':newList
                }
            
            
            
            
            return render(request, 'Blogs.html', data)
        else:
            pass

        
    data = {
        'department':dep,
        'blogs':blogs
    }
    
    return render(request, 'Blogs.html', data)


@login_required(login_url='/sign-in/')
def myBlogs(request):
    user_name = request.user
    user = UserProfile.objects.filter(user__username = user_name)
    doctor = DoctorProfile.objects.filter(user__username = user_name).first()
    data = Blog.objects.filter(profile = doctor)

    return render(request, 'MyBlogs.html', {
        'users':user.first(),
        'profile':doctor,
        'blogs':data
    })

@login_required(login_url='/sign-in/')
def writeBlog(request):
    user_name = request.user
    user = UserProfile.objects.filter(user__username = user_name)
    doctor = DoctorProfile.objects.filter(user__username = user_name)
    dep = Department.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        selected_category = request.POST.getlist('category')

        print(selected_category)
        data = Blog.objects.create(
            profile = doctor.first(),
            title = title,
            desc = content,
            category = selected_category
        )

        print('Data Created')
        data.save()
        print('Data Saved')
        return redirect(f'/profile/{user_name}')
        

    return render(request, 'WriteBlog.html', {
        'users':user.first(),
        'profile':doctor.first(),
        'dep':dep
    })

@login_required(login_url='/sign-in/')
def updateBlog(request, id):
    user_name = request.user
    data = Blog.objects.filter(id = id).first()
    if data.profile.user == user_name:
        user = UserProfile.objects.filter(user__username = user_name)
        doctor = DoctorProfile.objects.filter(user__username = user_name)

        if request.method == 'POST':
            data.title = request.POST.get('title')
            data.desc  = request.POST.get('content')

            data.save()
            return redirect('/blogs/manage/')
        
        return render(request, 'UpdateBlog.html', {
            'blog':data,
            'users':user.first(),
            'profile':doctor.first()
        })

@login_required(login_url='/sign-in/')
def deleteBlog(request, id):
    user_name = request.user
    data = Blog.objects.filter(id = id).first()
    if data.profile.user == user_name:
        data.delete()
        return redirect('/blogs/manage/')
