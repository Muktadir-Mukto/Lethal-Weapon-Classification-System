from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.models import User, auth
from .models import addpost
from .form import postform



class postView(ListView):
    model = addpost
    template_name = 'postView.html'

class addpost(CreateView):
    model = addpost
    form_class = postform
    template_name = "post.html"




