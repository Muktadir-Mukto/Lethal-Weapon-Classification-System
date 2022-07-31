from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    helpline = models.CharField(max_length=100)
