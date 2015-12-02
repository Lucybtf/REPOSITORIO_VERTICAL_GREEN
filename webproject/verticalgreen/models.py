from django.db import models
#from enum import Enum
from django_enumfield import enum
from datetime import datetime 
# Create your models here.

from bootstrap_themes import list_themes
from enum import IntEnum

#class MyModel(models.Model):
#	theme = models.CharField(default='default', choices=list_themes(),max_length=45)

class Proyecto(models.Model):
	name = models.CharField(max_length=45)
	def __unicode__(self):
		return 'Proyecto: ' + unicode(self.name)
	
class Perfil(models.Model):
	dni = models.CharField(max_length=9)
	name = models.CharField(max_length=45)
	def __unicode__(self):
		return 'Perfil: ' + self.dni + self.name

class Recurso(models.Model):
	name = models.CharField(max_length=45)
	tipo_recurso = models.CharField(max_length=45)
	def __unicode__(self):
		return 'Recurso: ' + self.name + " Tipo_recurso:" + self.tipo_recurso


class Nivel_Tarea(models.Model):
	nivel = models.IntegerField()
	def __unicode__(self):
		return unicode(self.nivel)

class Capacidad(models.Model):
	capacidad = models.CharField(max_length=30)
	def __unicode__(self):
		return self.capacidad

class Tipo_Tarea(models.Model):
	tipo_tarea = models.CharField(max_length=30)
	def __unicode__(self):
		return self.tipo_tarea
		
class Tarea(models.Model):
	name = models.CharField(max_length=250)
	proyecto = models.ForeignKey(Proyecto)
	tipo_accion = models.CharField(max_length=250)
	lugar = models.CharField(max_length=250)
	fecha = models.DateField(null=True, blank=True)
	capacidades = models.ManyToManyField(Capacidad)
	nivel = models.ForeignKey(Nivel_Tarea)
	recursos =models.ManyToManyField(Recurso)
	tipo_tarea = models.ForeignKey(Tipo_Tarea)
	unidades = models.IntegerField()
	tiempo = models.DecimalField(max_digits=5, decimal_places=2)
	facturado = models.DecimalField(max_digits=5, decimal_places=2)
	beneficio = models.DecimalField(max_digits=5, decimal_places=2)
	usuario = models.ForeignKey(Perfil)
	progreso = models.IntegerField()
	def __unicode__(self):
		return 'Tarea: ' + unicode(self.name) + '\n Proyecto' + unicode(self.proyecto) + '\nTipo:' + unicode(self.tipo_tarea) + '\nRecursos:' + unicode(self.recursos)
	#def get_recursos(self):
     #   return "\n".join([p.recursos for p in self.recursos.all()])
	def choices(self):
		return dict(Tarea.TIPO_TAREA)[self.tipo_tarea]
		
class Perfil_has_Tarea(models.Model):
	dni = models.CharField(max_length=9)
	tarea = models.ManyToManyField(Tarea)
	def __unicode__(self):
		return 'Perfil_has_tarea: ' + unicode(self.dni) + unicode(self.tarea)


#class Comercial(models.Model):
#	tarea = models.ForeignKey(Tarea)
#	proyecto = models.ForeignKey(Proyecto)
#	cliente = models.CharField(max_length=45)
#	direccion = models.CharField(max_length=45)
#	proveedor = models.CharField(max_length=45)
#	facturacion = models.DecimalField(max_digits=5, decimal_places=2)
#	beneficio = models.DecimalField(max_digits=5, decimal_places=2)
#	def __unicode__(self):
#		return 'Comercial: ' + unicode(self.cliente) + unicode(self.direccion) + unicode(self.proveedor) + unicode(self.facturacion) + unicode(self.beneficio)

#class Produccion(models.Model):
#	tarea = models.ForeignKey(Tarea)
#	proyecto = models.ForeignKey(Proyecto)
#	nivel = models.IntegerField()
#	tiempo = models.DecimalField(max_digits=5, decimal_places=2)
#	accion = models.CharField(max_length=45)
#	unidades = models.IntegerField()
#	beneficio = models.DecimalField(max_digits=5, decimal_places=2)
#	def __unicode__(self):
#		return 'Produccion: ' + unicode(self.nivel) + unicode(self.tiempo) + unicode(self.accion) + unicode(self.unidades) + unicode(self.beneficio)

#class Gestion(models.Model):
#	tarea = models.ForeignKey(Tarea)
#	proyecto = models.ForeignKey(Proyecto)
#	beneficio = models.DecimalField(max_digits=5, decimal_places=2)
#	def __unicode__(self):
#		return 'Gestion: ' + unicode(self.beneficio)

#class Diseno(models.Model):
#	tarea = models.ForeignKey(Tarea)
#	proyecto = models.ForeignKey(Proyecto)
#	beneficio = models.DecimalField(max_digits=5, decimal_places=2)
#	def __unicode__(self):
#		return 'Diseno: ' + unicode(self.beneficio)