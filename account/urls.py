from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('sign-in/', views.SignIn, name='sign-in'),
    path('register/', views.Register, name='register')
]