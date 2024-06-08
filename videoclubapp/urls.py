from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("personas/", views.personas, name="personas"),
    path("contacto/", views.contacto, name="contacto"),
]