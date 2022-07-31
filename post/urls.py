from django.urls import path, include

from . import views
from .views import addpost, postView
from django.contrib.auth.models import User, auth


urlpatterns = [
    path('postView',postView.as_view(), name="postView"),
    path('addpost', addpost.as_view(), name="addpost"),
    path('', include('home_menu.urls'), name="/"),


]
