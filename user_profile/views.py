from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User, auth




def index(request):
    return render(request, "index.html")


def profile_edit(request,id=None):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_Number = request.POST['phone_Number']
        location = request.POST['location']
        website = request.POST['website']

        user = User.objects.create_user(email=email,first_name=first_name, last_name=last_name, website=website, location= location, phone_Number=phone_Number)
        user.save();
        return redirect('/SIGNUP_LOGIN/profile')
    else:
        return render(request, "profile_edit.html", {'link': '/'})



