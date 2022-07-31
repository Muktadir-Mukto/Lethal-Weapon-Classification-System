from django.db import models
from django.contrib.auth.models import User, auth


# Create your models here.

class Userprofile(models.Model):
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="_")
    img = models.ImageField(upload_to='img', default="_")
    occupation = models.CharField(max_length=100, default="_")
    phone = models.CharField(max_length=100, default="_")
    birthday = models.CharField(max_length=100, default="_")
    class Meta:
        db_table = "signup_login_userprofile"





