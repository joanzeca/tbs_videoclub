from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("personas/", views.personas, name="personas"),
    path("contacto/", views.contacto, name="contacto"),
    path("personas/registrar/", views.registrar_persona, name="registrar_persona"),
    path("success/", views.success, name="success"),
    path('personas/editar/<int:id>/', views.editar_persona, name='editar_persona'),
    path('personas/eliminar/<int:id>/', views.eliminar_persona, name='eliminar_persona'),
]