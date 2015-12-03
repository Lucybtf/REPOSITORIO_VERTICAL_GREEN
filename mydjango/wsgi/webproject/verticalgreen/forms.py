from django.db import models
from django import forms
from django.forms import ModelForm
from verticalgreen.models import  Recurso, Tarea

class TareaForm(ModelForm):
	class Meta:
		model = Tarea	
		fields = ['name', 'proyecto', 'tipo_accion', 'lugar', 'fecha', 'capacidades', 'nivel', 'recursos', 'tipo_tarea', 'unidades', 'tiempo', 'facturado', 'beneficio', 'usuario', 'progreso']


		
#class RecursoForm(forms.ModelForm):
	#name = forms.CharField(required=True)
#	class Meta:
#		model = Recurso	
#		fields = ['name', 'tipo_recurso']
		
	#def clean_recurso(self):
	#	diccionario_limpio = self.cleaned_data
	#	recurso = diccionario_limpio.get('recurso')
	#	if len(recurso) < 0:
	#		raise forms.ValidationError("El recurso esta vacio")
	#	return autor	

