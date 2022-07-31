from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, DetailView
from .models import Crime


def crime(request):
    cri = Crime.objects.all()
    return render(request, "Weapon.html" ,{'cri' : cri})


class detail1(DetailView):
    model = Crime
    template_name = 'c_details.html'