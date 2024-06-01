from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("nosotros/", views.nosotros),
    path("servicios/", views.servicios),
    path("contacto/", views.contacto),
]