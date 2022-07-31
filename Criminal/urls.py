from django.urls import path, include

from . import views
from .views import detail2

urlpatterns = [
    path("criminal", views.criminal, name="criminal"),
    path("detail2/<int:pk>", detail2.as_view(), name="detail2"),
]