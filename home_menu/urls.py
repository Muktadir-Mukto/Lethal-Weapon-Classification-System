from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('upload', views.upload, name="upload")
]