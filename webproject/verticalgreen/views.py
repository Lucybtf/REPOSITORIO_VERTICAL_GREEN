from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

from verticalgreen.models import Proyecto


def inicio(request):
    #recetas = Receta.objects.all()
	#template=loader.get_template('template/index.html')
    return render_to_response('index.html')

def login(request):
    #recetas = Receta.objects.all()
	#template=loader.get_template('template/index.html')
    return render_to_response('login.html')

def tareas(request):
    #recetas = Receta.objects.all()
	#template=loader.get_template('template/index.html')
    return render_to_response('ui.html')
