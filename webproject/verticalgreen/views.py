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
from verticalgreen.models import Proyecto, Perfil, Perfil_has_Tarea, Tarea, Recurso, Comercial, Produccion, Gestion, Diseno
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
	
	#recursos = Recurso.objects.all()
	#return render_to_response('ui.html', {'tareas': tareas})
#	db = MySQLdb.connect(user='root', db='webproject', passwd='', host='localhost')
#	cursor = db.cursor()
#	qkeys = ['tarea','proyecto','tipo_tarea','recurso', 'tipo']
#	cursor.execute('SELECT verticalgreen_tarea.name as tarea, verticalgreen_proyecto.name as proyecto,  verticalgreen_tarea.tipo_tarea, verticalgreen_recurso.name, verticalgreen_recurso.tipo_recurso FROM `verticalgreen_tarea`, `verticalgreen_tarea_recursos`, `verticalgreen_recurso`, `verticalgreen_proyecto` where recurso_id = verticalgreen_recurso.id && verticalgreen_tarea.id = tarea_id && verticalgreen_proyecto.id = verticalgreen_tarea.proyecto_id')
#	tareas = cursor.fetchall()
#	print tareas
#	fdicts = []
#	for row in tareas:
#		i = 0
#		cur_row = {}
#		for key in qkeys:
#			cur_row[key] = row[i]
#			i = i+1
#		fdicts.append(cur_row) 
#	db.close()
	print request.method
	if request.method == 'POST':
		tareas = Tarea.objects.all()
		idtareaborrar = request.POST['tarea']
		print idtareaborrar
		print Tarea.objects.get(id=idtareaborrar);
		Tarea.objects.get(id=idtareaborrar).delete();
		return render_to_response('tareas.html', {'tareas': tareas}, context_instance=RequestContext(request))
	else:
		tareas = Tarea.objects.all()
		print "HOLA"
		print request.method
		return render_to_response('tareas.html', {'tareas': tareas}, context_instance=RequestContext(request))

#Ejemplo de actualizacion de un objeto django		
#def update(request, id):
#    link = Link.objects.get(id=id)
#    link.link_description = request.POST["link_description"]
#    link.link_url = request.POST["link_url"]
#    link.save()
#    return list(request, message="Link updated!")
	
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
#def login(request):
#    return render_to_response('login.html',{}, context_instance=RequestContext(request))

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
			return render(request, 'formtarea.html', {'form_tarea': form_tarea})

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
                                      




	
#def post_form_upload(request):
 #   if request.method == 'GET':
  #      form = PostForm()
   # else:
        # A POST request: Handle Form Upload
    #    form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
     #   # If data is valid, proceeds to create a new post and redirect the user
     #   if form.is_valid():
     #       content = form.cleaned_data['content']
     #       created_at = form.cleaned_data['created_at']
      #      post = m.Post.objects.create(content=content,
      #                                   created_at=created_at)
      #      return HttpResponseRedirect(reverse('post_detail',
                     #                           kwargs={'post_id': post.id}))
 
    #return render(request, 'form.html', {
    #    'form': form,
    #})
	
