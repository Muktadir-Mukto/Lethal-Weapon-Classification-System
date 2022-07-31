from django.urls import path, include

from . import views
from .views import detail1

urlpatterns = [
    path("Weapon", views.crime, name="Weapon"),
    path("detail1/<int:pk>", detail1.as_view(), name="detail1"),


]
