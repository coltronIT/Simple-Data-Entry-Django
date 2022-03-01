from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.item, name="item"),
    path("confirmation/", views.confirmation, name="confirmation"),
]