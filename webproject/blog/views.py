#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from blog.forms import PostForm
from blog.models import Post
 
 
def create_post(request):
	#si es una peticion post
    if request.method == "POST":
    	#asignamos a form el formulario para validar
        form = PostForm(request.POST)
        #si el formulario es validado correctamente
        if form.is_valid():
        	#creamos una nueva instancia de Post con los campos del form
        	#asi capturamos los valores post
        	newPost = Post(title = request.POST["title"], url = request.POST["url"], content = request.POST["content"])
        	#guardamos el post
        	newPost.save()
        	#redirigimos a la ruta con name add_post, que es esta
        	return redirect('add_post')
    else:
    	#si no es una peticion post, asignamos a form 
    	#el form que hemos creado sin datos
        form = PostForm()
    #siempre devolvemos la misma respuesta
    return render_to_response("crear_post.html",{"form":form}, context_instance = RequestContext(request))