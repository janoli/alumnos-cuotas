from django.db import models

# Create your models here.

class Alumno(models.Model):
    apellido_text = models.CharField(max_length=40)
    nombre_text = models.CharField(max_length=40)
    dni_text = models.CharField(max_length=11)

    def __str__(self):
        return self.apellido_text + ", " + self.nombre_text
