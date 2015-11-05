#from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,authenticate, logout
from django.contrib.auth.decorators import login_required

from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.template import Context, loader
from django.template.context import RequestContext
from django.shortcuts import render_to_response
import MySQLdb
from django.db import connection
print connection.queries
from verticalgreen.models import Tarea, Recurso

def inicio(request):
    return render_to_response('index.html')

def login(request):
    return render_to_response('login.html',{}, context_instance=RequestContext(request))

def tareas(request):
	#tareas = Tarea.objects.all()
	#recursos = Recurso.objects.all()
	#return render_to_response('ui.html', {'tareas': tareas})
	db = MySQLdb.connect(user='root', db='webproject', passwd='', host='localhost')
	cursor = db.cursor()
	qkeys = ['tarea','proyecto','tipo_tarea','recurso', 'tipo']
	cursor.execute('SELECT verticalgreen_tarea.name as tarea, verticalgreen_proyecto.name as proyecto,  verticalgreen_tarea.tipo_tarea, verticalgreen_recurso.name, verticalgreen_recurso.tipo_recurso FROM `verticalgreen_tarea`, `verticalgreen_tarea_recursos`, `verticalgreen_recurso`, `verticalgreen_proyecto` where recurso_id = verticalgreen_recurso.id && verticalgreen_tarea.id = tarea_id && verticalgreen_proyecto.id = verticalgreen_tarea.proyecto_id')
	tareas = cursor.fetchall()
	fdicts = []
	for row in tareas:
		i = 0
		cur_row = {}
		for key in qkeys:
			cur_row[key] = row[i]
			i = i+1
		fdicts.append(cur_row) 
	db.close()
	return render_to_response('ui.html', {'tareas': fdicts})
	
def nuevo_usuario(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('nuevousuario.html',{'formulario': formulario}, context_instance=RequestContext(request))

def ingresar(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso =authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					auth_login(request, acceso)
					return HttpResponseRedirect('/')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario =AuthenticationForm()
	return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
