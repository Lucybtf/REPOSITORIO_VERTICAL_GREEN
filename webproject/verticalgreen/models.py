from django.db import models

# Create your models here.

from bootstrap_themes import list_themes

class MyModel(models.Model):
	theme = models.CharField(default='default', choices=list_themes(),max_length=45)

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
		return 'Recurso: ' + self.name + self.tipo_recurso
	
class Tarea(models.Model):
	name= models.CharField(max_length=45)
	proyecto = models.ForeignKey(Proyecto)
	COMERCIAL = 'Comercial'
	PRODUCCION = 'Produccion'
	GESTION = 'Gestion'
	DISENO = 'Diseno'
	TIPO_TAREA = (
		(COMERCIAL, 'Comercial'),
		(PRODUCCION, 'Produccion'),
		(GESTION, 'Gestion'),
		(DISENO, 'Diseno'),
    )
	tipo_tarea = models.CharField(max_length=20, choices=TIPO_TAREA, default=PRODUCCION)
	recursos =models.ManyToManyField(Recurso)
	def __unicode__(self):
		return 'Tarea: ' + unicode(self.name) + unicode(self.proyecto)
	
class Perfil_has_Tarea(models.Model):
	dni = models.CharField(max_length=9)
	tarea = models.ManyToManyField(Tarea)
	def __unicode__(self):
		return 'Perfil_has_tarea: ' + unicode(self.dni) + unicode(self.tarea)


class Comercial(models.Model):
	tarea = models.ForeignKey(Tarea)
	proyecto = models.ForeignKey(Proyecto)
	cliente = models.CharField(max_length=45)
	direccion = models.CharField(max_length=45)
	proveedor = models.CharField(max_length=45)
	facturacion = models.DecimalField(max_digits=5, decimal_places=2)
	beneficio = models.DecimalField(max_digits=5, decimal_places=2)
	def __unicode__(self):
		return 'Comercial: ' + unicode(self.cliente) + unicode(self.direccion) + unicode(self.proveedor) + unicode(self.facturacion) + unicode(self.beneficio)

class Produccion(models.Model):
	tarea = models.ForeignKey(Tarea)
	proyecto = models.ForeignKey(Proyecto)
	nivel = models.IntegerField()
	tiempo = models.DecimalField(max_digits=5, decimal_places=2)
	accion = models.CharField(max_length=45)
	unidades = models.IntegerField()
	beneficio = models.DecimalField(max_digits=5, decimal_places=2)
	def __unicode__(self):
		return 'Produccion: ' + unicode(self.nivel) + unicode(self.tiempo) + unicode(self.accion) + unicode(self.unidades) + unicode(self.beneficio)

class Gestion(models.Model):
	tarea = models.ForeignKey(Tarea)
	proyecto = models.ForeignKey(Proyecto)
	beneficio = models.DecimalField(max_digits=5, decimal_places=2)
	def __unicode__(self):
		return 'Gestion: ' + unicode(self.beneficio)

class Diseno(models.Model):
	tarea = models.ForeignKey(Tarea)
	proyecto = models.ForeignKey(Proyecto)
	beneficio = models.DecimalField(max_digits=5, decimal_places=2)
	def __unicode__(self):
		return 'Diseno: ' + unicode(self.beneficio)