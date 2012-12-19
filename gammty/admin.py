from django.contrib import admin
from gammty.models import Nosotros, Objetivo, Cliente, Servicio, Tipo, SSC_inscripcion

class NosotrosAdmin(admin.ModelAdmin):
	pass

admin.site.register(Nosotros, NosotrosAdmin)

class ObjetivoAdmin(admin.ModelAdmin):
	list_display = ('descripcion',)
	list_display_links = ('descripcion',)

admin.site.register(Objetivo, ObjetivoAdmin)

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	list_display_links = ('nombre',)

admin.site.register(Cliente, ClienteAdmin)

class ServicioAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	list_display_links = ('nombre',)

admin.site.register(Servicio, ServicioAdmin)

class TipoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	list_display_links = ('nombre',)

admin.site.register(Tipo, TipoAdmin)

class SSCAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'matricula', 'semestre', 'carrera', 
		'correo', 'telefono', 'porque', 'como_te_enteraste',
		'comentarios', 'fecha')
	list_display_links = ('nombre', 'matricula')

admin.site.register(SSC_inscripcion, SSCAdmin)