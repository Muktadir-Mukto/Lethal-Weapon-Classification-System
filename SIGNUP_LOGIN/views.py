from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.models import User, auth
from SIGNUP_LOGIN.models import Userprofile
from .forms import update_user



def SIGNUP(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken! Try again.')
                return redirect('SIGNUP')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken! Try again.')
                return redirect('SIGNUP')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)

                saverecord=Userprofile()
                saverecord.email=request.POST.get('email')
                saverecord.save()
                user.save()
                return redirect('LOGIN')

        else:
            messages.info(request, 'Confirm Password not matching! Try again.')
            return redirect('SIGNUP')
    else:
        return render(request, "SIGNUP.html")



def LOGIN(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('LOGIN')

    else:
        return render(request, "LOGIN.html")




def LOGOUT(request):
    auth.logout(request)
    return redirect('/')




def Userprofile1(request,pk):
    up = Userprofile.objects.get(pk=pk)
    return render(request,"profile.html",{"up":up})




def Update_profile(request,pk):
    up = Userprofile.objects.get(pk=pk)
    return render(request,"profile_edit.html",{"up":up})



def Up_profile(request,pk):
    update = Userprofile.objects.get(pk=pk)
    form=update_user(request.POST,instance=update)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return redirect('/')



