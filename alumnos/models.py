# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Alumno(models.Model):
    apellidos = models.CharField(max_length=40)
    nombres = models.CharField(max_length=40)
    dni = models.CharField(max_length=11)
    email = models.EmailField(null=True)
    fecha_inicio = models.DateField(null=True)
    fecha_nacimiento = models.DateField(null=True)
    telefono_particular = models.CharField(max_length=40, blank=True)
    telefono_movil = models.CharField(max_length=40, blank=True)
    dirección = models.CharField(max_length=40, blank=True)
    ciudad = models.CharField(max_length=40, blank=True)
    provincia = models.CharField(max_length=40, blank=True)
    convenio = models.BooleanField(default=False)

    def __str__(self):
        return self.apellidos + ", " + self.nombres

class Curso(models.Model):
    curso = models.CharField(max_length=40)
    año = models.CharField(max_length=4)
    cuota = models.DecimalField(max_digits=12, decimal_places=2)
    derexam = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.curso + " (" + self.año + ")"

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    cursando = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.alumno.apellidos + ", " + self.alumno.nombres + " @ " +self.cursando.curso
