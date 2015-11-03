from django.contrib import admin

# Register your models here.

from verticalgreen.models import Proyecto, Perfil, Perfil_has_Tarea, Tarea, Recurso, Comercial, Produccion, Gestion, Diseno
  
admin.site.register(Proyecto)
admin.site.register(Perfil)
admin.site.register(Tarea)
admin.site.register(Perfil_has_Tarea)
admin.site.register(Recurso)
#admin.site.register(Tarea_has_Recurso)
admin.site.register(Comercial)
admin.site.register(Produccion)
admin.site.register(Gestion)
admin.site.register(Diseno)