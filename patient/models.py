from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    district = models.CharField(max_length=120, default=None)
    state = models.CharField(max_length=100, default=None)
    healthCard = models.CharField(max_length=100, default=None)
    desc = models.TextField(max_length=150, default=None)

