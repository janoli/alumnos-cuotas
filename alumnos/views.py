from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Alumno
# Create your views here.

def index(request):
    latest_alumno_list = Alumno.objects.all()
    template = loader.get_template('alumnos/index.html')
    context = {
            'latest_alumno_list': latest_alumno_list,
            }
    return HttpResponse(template.render(context, request))

