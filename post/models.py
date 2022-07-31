from django.db import models
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth



# Create your models here.

class addpost(models.Model):
    Post= models.TextField()


    def get_absolute_url(self):
        return redirect('/',args=(str(self.id)))




