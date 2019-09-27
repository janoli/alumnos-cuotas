# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Alumno(models.Model):
    apellido_text = models.CharField(max_length=40)
    nombre_text = models.CharField(max_length=40)
    dni_text = models.CharField(max_length=11)

    def __str__(self):
        return self.apellido_text + ", " + self.nombre_text

class Curso(models.Model):
    curso_text = models.CharField(max_length=40)
    año_text = models.CharField(max_length=4)
    cuota_text = models.IntegerField(null=True)
    derexam_text = models.IntegerField(null=True)

    def __str__(self):
        return self.curso_text + " (" + self.año_text + ")"

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    cursando = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.alumno.apellido_text + ", " + self.alumno.nombre_text + "@" +self.cursando.curso_text
