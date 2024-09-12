from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    slug = AutoSlugField(unique=True, null=True, populate_from = 'name', default=None)

    def __str__(self) -> str:
        return self.name
    
    