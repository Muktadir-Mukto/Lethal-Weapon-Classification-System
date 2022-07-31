from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, DetailView
from .models import Criminal


def criminal(request):
    crin = Criminal.objects.all()
    return render(request, "Lethal-Weapon.html" ,{'crin' : crin})

class detail2(DetailView):
    model = Criminal
    template_name = 'cr_details.html'

