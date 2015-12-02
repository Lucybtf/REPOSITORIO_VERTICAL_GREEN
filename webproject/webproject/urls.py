"""webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from verticalgreen import views

# Uncomment the next two lines to enable the admin:
admin.autodiscover()


urlpatterns = [
	#url('', include('django.contrib.auth.urls')),
	#PESTANAS WEB
	url(r'^recursos/$', 'verticalgreen.views.recursos'), #RECURSOS
	url(r'^tareas/$', 'verticalgreen.views.tareas'), #PROYECTOS
	url(r'^proyectos/$', 'verticalgreen.views.proyectos'), #TAREAS
	url(r'^$', 'verticalgreen.views.inicio'), #PERFIL
	url(r'^/logout$', 'verticalgreen.views.logout'),
	#FORMULARIOS
	url(r'^usuario/nuevo$','verticalgreen.views.nuevo_usuario'), #FORMULARIO REGISTRO
	url(r'^login/$','verticalgreen.views.login'), #FORMULARIO LOGIN
	url (r'^tareas/newtarea/', 'verticalgreen.views.newtarea'), #FORMULARIO NUEVATAREA
	url (r'^tareas/editartarea/', 'verticalgreen.views.editartarea'), #FORMULARIO EDITARTAREA
	url (r'^tareas/update/', 'verticalgreen.views.updatetarea'), #FORMULARIO UPDATETAREA
	#ADMIN
	url(r'^admin/', include(admin.site.urls)),
	#url(r'^prueba/','verticalgreen.views.post_form_upload')
	#url(r'^add_post/', 'blog.views.create_post', name='add_post'),
]
