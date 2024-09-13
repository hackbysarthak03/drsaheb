"""
URL configuration for drsaheb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'drsaheb'

urlpatterns = [
    path('admin-panel-vsarthak62/', admin.site.urls),
    path('', views.Home, name='home'),
    path('sign-out', views.signOut, name='sign-out'),
    path('about-us/', views.About, name='about'),
    path('services/', views.Services, name='services'),
    path('my-bookings/', views.bookings, name='bookings'),
    path('services/<slug>', views.depart),
    path('blogs/', include('blog.urls')),
    path('our-heroes/', include('doctor.urls')),
    path('', include('account.urls')),
    path('meet/', include('videoconference.urls')),
    path('update/<user_name>', views.updateProfile),
    path('profile/<user_name>', views.profile),
    path('', include('bookings.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
