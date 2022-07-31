from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("profile_edit", views.profile_edit, name="profile_edit"),

]