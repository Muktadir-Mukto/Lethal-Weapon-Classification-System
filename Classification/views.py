from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User, auth
from .models import Department


def department(request):
    dep  = Department.objects.all()
    return render(request, "Classification.html" ,{'dep' : dep})


class detail(DetailView):
    model = Department
    template_name = 'd_details.html'
