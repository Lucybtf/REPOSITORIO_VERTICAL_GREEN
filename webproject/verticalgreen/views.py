from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.template import Context, loader
from django.template.context import RequestContext
from django.shortcuts import render_to_response
import MySQLdb
from django.db import connection
print connection.queries
from django.template.defaultfilters import register
from verticalgreen.models import Proyecto, Perfil, Perfil_has_Tarea, Tarea, Recurso, Capacidad, Nivel_Tarea, Tipo_Tarea
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt 
from django.core.mail import send_mail
from verticalgreen.forms import  TareaForm
from django.shortcuts import render

#PESTANAS WEB
#RECURSOS. Muestra la tabla de recursos.
def recursos(request):
	recursos = Recurso.objects.all()
	return render_to_response('recursos.html',{'recursos': recursos})
	

#TAREAS. Muestra la tabla de tareas.
def tareas(request):


	if request.method == 'POST' and 'deletetarea' in request.POST:
		tareas = Tarea.objects.all()
		idtareaborrar = request.POST['deletetarea']
		#print idtareaborrar
		Tarea.objects.get(id=idtareaborrar).delete();
		return render_to_response('tareas.html', {'tareas': tareas}, context_instance=RequestContext(request)) 
	
	if request.method == 'POST' and 'editartarea' in request.POST:
		idtareaeditar = request.POST['editartarea']
		#print "ID TAREA"
		#print idtareaeditar
		request.session['idtareaeditar']= idtareaeditar
		
		return redirect('/tareas/editartarea/', tareaid=idtareaeditar)
	
	else:
		tareas = Tarea.objects.all()
		return render_to_response('tareas.html', {'tareas': tareas}, context_instance=RequestContext(request))

		
		
#Ejemplo de actualizacion de un objeto django		
#def update(request, id):
#    link = Link.objects.get(id=id)
#    link.link_description = request.POST["link_description"]
#    link.link_url = request.POST["link_url"]
#    link.save()
#    return list(request, message="Link updated!")
#editar tarea

#PROYECTOS. Muestra la tabla de recursos.
def proyectos(request):
	proyectos = Proyecto.objects.all()
	return render_to_response('proyectos.html', {'proyectos': proyectos})

#PERFIL. Muestra el perfil del usuario.	
def inicio(request):
    return render_to_response('index.html')

#LOGOUT.	
def logout(request):
	return render_to_response('login.html')

#REGISTRO NUEVO USUARIO. Crea el formulario de registro del usuario.
def nuevo_usuario(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm() #nuevousuario.html
	return render_to_response('registrarnuevousuario.html',{'formulario': formulario}, context_instance=RequestContext(request))


#LOGIN
def login(request):
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
				else: #SI NO ESTA ACTIVO
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else: #SI NO ES USUARIO
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario =AuthenticationForm()#ingresar.html
	return render_to_response('loginusuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

#NUEVA TAREA
def newtarea(request):
		if request.method == 'POST':
			tarea_form=TareaForm(request.POST)
			print request.POST
			#print tarea_form.is_valid
			if tarea_form.is_valid():
				print "HOLA"
				tarea_form.save()
				html="Formulario enviado"
				return HttpResponse(html)
				#return render_to_response('index.html', {'formulario': recurso_form})
			else:
				print request.POST
				return HttpResponse("Formulario no correcto")
		else:
			#Formulario Vacio
			#form_recurso = RecursoForm()
			form_tarea = TareaForm()
			Capacidades = Capacidad.objects.all()
			Proyectos = Proyecto.objects.all() 
			Recursos = Recurso.objects.all()
			return render(request, 'formtarea.html', {'form_tarea': form_tarea, 'capacidades': Capacidades, 'proyectos': Proyectos, 'recursos': Recursos })

#BORRAR TAREA			
def deletetarea(request):
		if request.method == 'POST':
			tarea_form=TareaForm(request.POST)
			if tarea_form.is_valid():
				tarea_form.save()
				html="Formulario enviado"
				return HttpResponse(html)
				#return render_to_response('index.html', {'formulario': recurso_form})
			else:
				return HttpResponse("Formulario no correcto")
		else:
			#Formulario Vacio
			#form_recurso = RecursoForm()
			form_tarea = TareaForm()
			return render(request, 'form.html', {'form_tarea': form_tarea})

#EDITAR TAREA			
def editartarea(request):
	idtarea = request.session.get('idtareaeditar')
	tareaeditada = Tarea.objects.get(id=idtarea)
	nocapacidades = []
	print tareaeditada.tipo_tarea
	for i in Capacidad.objects.all():
		nocapacidades.insert(i.id, i)
	for i in tareaeditada.capacidades.all():
		nocapacidades.remove(i)
	noseleccionados =[]
	for i in Recurso.objects.all():
		noseleccionados.insert(i.id,i)
	for i in tareaeditada.recursos.all():
		noseleccionados.remove(i)
	
	return render_to_response('formeditartarea.html',{'tarea': tareaeditada, 'totalproyectos': Proyecto.objects.all(), 'totalusuarios': Perfil.objects.all(), 'totaltipotareas':Tipo_Tarea.objects.all(), 'things': tareaeditada.capacidades.all() ,'totalcapacidades': nocapacidades, 'nivel': Nivel_Tarea.objects.all(), 'recursos':noseleccionados }, context_instance=RequestContext(request))

#UPDATE TAREA	
def updatetarea(request):

	if request.method == 'POST':
		idtarea = request.session.get('idtareaeditar')
		#print "TAREA ID EN ACTUALIZACION"
		#print idtarea
		tareaup = Tarea.objects.get(id=idtarea)
		
		# print "NOMBRE"
		# print request.POST["name"]
		# print "PROYECTO"
		# print request.POST["proyecto"]
		# print "TIPO_ACCION"
		# print request.POST["tipo_accion"]
		# print "LUGAR"
		# print request.POST["lugar"]
		# print "FECHA"
		# print request.POST["fecha"]
		# print "CAPACIDADES:"
		# print request.POST.getlist("capacidades[]")
		# print "NIVEL"
		# print request.POST["nivel"]
		# print "UNIDADES"
		# print request.POST["unidades"]
		# print "TIEMPO"
		# print request.POST["tiempo"]
		# print "FACTURADO"
		# print request.POST["facturado"]
		# print "BENEFICIO"
		# print request.POST["beneficio"]
		# print "PROGRESO"
		# print request.POST["progreso"]
		# print "RECURSOS"
		# print request.POST.getlist('recursos')
		# print "USUARIO"
		# print request.POST["usuario"]
		# print "TIPO DE TAREA"
		# print request.POST["tipo_tarea"]
		listcapacidades = []
		listcapacidades = request.POST.getlist('capacidades[]')
		tareaup.capacidades.remove()
		for i in listcapacidades:
			capacidad = Capacidad.objects.get(id=i)
			tareaup.capacidades.add(capacidad)
		listrecursos = []
		listrecursos = request.POST.getlist('recursos[]')
		tareaup.recursos.remove()
		# print "LISTA DE RECURSOS"
		for i in listrecursos:
			recurso = Recurso.objects.get(id=i)
			tareaup.recursos.add(recurso)
		tareaup.name = request.POST["name"]
		tareaup.proyecto = Proyecto(id=request.POST["proyecto"])
		tareaup.tipo_accion = request.POST["tipo_accion"]
		tareaup.lugar = request.POST["lugar"]
		tareaup.fecha = request.POST["fecha"]
		#tareaup.capacidades = Capacidad(request.POST.getlist('capacidades[]'))
		tareaup.nivel = Nivel_Tarea.objects.get(nivel=request.POST['nivel'])
		#tareaup.recursos = Recurso(request.POST.getlist('recursos'))
		# print "TIPO TAREA"
		#print request.POST["tipo_tarea"]
		tareaup.tipo_tarea = Tipo_Tarea.objects.get(id=request.POST["tipo_tarea"])
	#	tareaup.tipo_tarea = Tipo_Tarea.objects.get(id=request.POST['tipo_tarea'])
		tareaup.unidades = request.POST['unidades']
		tareaup.tiempo = request.POST['tiempo']
		tareaup.facturado = request.POST['facturado']
		tareaup.beneficio = request.POST['beneficio']
		tareaup.usuario = Perfil(id=request.POST['usuario'])
		tareaup.progreso = request.POST['progreso']
	#	print tareaup.capacidades.recurso_set.add(Capacidad.objects.get(id=1))	
#    link.link_url = request.POST["link_url"]
		tareaup.save()
		return HttpResponse("Tarea actualizada")	
	#else:
		#print "HOLA"
	#idtareaeditar = request.POST['edittarea']
	#print idtareaeditar
	#tareaeditada = Tarea.objects.get(id=idtareaeditar);
		#	tareaeditada.proyecto = request.POST["name"]
			#tareaeditada.name = request.POST["name"]
	#print tareaeditada
	#return render_to_response('formeditartarea.html', {'action': editartarea,'id': id, 'name':tareaeditada.name, 'proyecto': tareaeditada.proyecto, 'tipo_tarea': tareaeditada.tipo_tarea, 'recursos':tareaeditada.recursos}, context_instance=RequestContext(request))
	