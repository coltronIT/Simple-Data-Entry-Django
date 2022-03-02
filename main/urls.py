from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("confirmation/<int:id>", views.confirmation, name="confirmation"),
]