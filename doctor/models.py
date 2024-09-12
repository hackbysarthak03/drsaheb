from django.db import models
from django.contrib.auth.models import User
from department.models import *

# Create your models here.

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=10)
    specialist = models.CharField(max_length=100)
    desc = models.TextField(max_length=200, default=None)
    degree = models.CharField(max_length=200)
    hospital = models.CharField(max_length=150)
    hospital_district = models.CharField(max_length=150)
    hospital_state = models.CharField(max_length=150)
    fees = models.CharField(max_length=50)
    avail = models.BooleanField(default=False)
    room_id = models.CharField(max_length=100, default='--')

    
    

