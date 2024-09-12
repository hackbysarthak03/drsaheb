from django.db import models
from doctor.models import *
from django.utils import timezone

# Create your models here.


class Blog(models.Model):
    profile = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    category = models.JSONField(default=list, blank=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.profile} -- {self.created_on}'

