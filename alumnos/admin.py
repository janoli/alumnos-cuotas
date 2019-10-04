from django.contrib import admin

from .models import Alumno, Curso, Inscripcion
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    search_fields = ['apellidos', 'nombres', 'dni']
    list_display = ('apellidos', 'nombres', 'dni', 'email')

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Curso)
admin.site.register(Inscripcion)
