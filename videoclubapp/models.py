from django.db import models

# Create your models here.

class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()
    edad = models.IntegerField()
    sueldo = models.DecimalField(max_digits=6, decimal_places=2)
    rnd = models.CharField(max_length=50)
    estado = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"