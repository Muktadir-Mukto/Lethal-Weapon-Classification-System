from django.urls import path, include

from . import views
from .views import Userprofile1, Update_profile
from django.contrib.auth.models import User, auth


urlpatterns = [
    path("SIGNUP", views.SIGNUP, name="SIGNUP"),
    path("LOGIN", views.LOGIN, name="LOGIN"),
    path("LOGOUT", views.LOGOUT, name="LOGOUT"),
    path("Userprofile1/<int:pk>", views.Userprofile1, name="Userprofile1"),
    path("Userprofile1/edit/<int:pk>", views.Update_profile, name="Update_profile"),
    path("update/<int:pk>", views.Up_profile, name="Up_profile"),
]

