from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("programas/", views.programas),
    path("talleres/", views.talleres),
    path("asesoramiento/", views.asesoramiento),
    path("contacto/", views.contacto),
]