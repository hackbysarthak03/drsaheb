from django.db import models

# Create your models here.

class Testimonial(models.Model):
    user = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    desc = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.user
