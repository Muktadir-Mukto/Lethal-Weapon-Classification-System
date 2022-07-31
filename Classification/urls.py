from django.urls import path, include
from . import views
from .views import detail

urlpatterns = [
    path("Classification", views.department, name="Classification"),
    path("detail/<int:pk>", detail.as_view(), name="detail"),


]