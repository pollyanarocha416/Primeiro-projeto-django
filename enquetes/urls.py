from django.urls import path
from enquetes import views

urlpatterns = [
    path("", views.home, name="home"),
    path("enquetes/<name>", views.enquetes_there, name="enquetes_there"),
]
