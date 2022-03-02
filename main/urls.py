from django.urls import path

from . import views

urlpatterns = [
    path("", views.create, name="create"),
    path("confirmation/<int:id>", views.confirmation, name="confirmation"),
]