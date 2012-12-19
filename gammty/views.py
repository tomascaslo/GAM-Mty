from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from datetime import date

from gammty.models import Nosotros, Objetivo, Cliente, Servicio, SSC_inscripcion
from gammty.forms import ContactoForm, SSCForm, SSCCrispyForm

def index(request):
	return render_to_response('main.html', {}, context_instance=RequestContext(request))

def nosotros_vista(request):
	nosotros = Nosotros.objects.all()
	objetivos = Objetivo.objects.filter(nosotros=nosotros)

	return render_to_response('nosotros.html', {
		'nosotros': nosotros,
		'objetivos': objetivos
		}, context_instance=RequestContext(request))

def quienes_somos_vista(request):
	return render_to_response('quienes.html', {}, context_instance=RequestContext(request))

def historia_vista(request):
	return render_to_response('historia.html', {}, context_instance=RequestContext(request))

def sem_aguilas_vista(request):
	return render_to_response('seminar-aguilas.html', {}, context_instance=RequestContext(request))

def sem_qim_vista(request):
	return render_to_response('seminar-QiM.html', {}, context_instance=RequestContext(request))

def dia_aguilas_vista(request):
	return render_to_response('dia-aguilas.html', {}, context_instance=RequestContext(request))

def cipa_caipa_vista(request):
	return render_to_response('CIPA-CAIPA.html', {}, context_instance=RequestContext(request))

def servicios_vista(request):
	servicios = Servicio.objects.order_by('tipo')

	return render_to_response('servicios.html', {
		'servicios': servicios
		}, context_instance=RequestContext(request))

def escuela_vista(request):
	return render_to_response('escuela.html', {}, context_instance=RequestContext(request))

"""
def  clientes_vista(request):
	clientes = Cliente.objects.all()

	return render_to_response('clientes.html', {
		'clientes': clientes
		}, context_instance=RequestContext(request))
"""

def ssc_vista(request):
	return render_to_response('ssc.html', {}, context_instance=RequestContext(request))

def ssc_form_vista(request):
	if request.method == 'POST':
		form = SSCForm(request.POST)

		if form.is_valid():
			new_ssc = SSC_inscripcion()
			new_ssc.nombre = form.cleaned_data['nombre']
			new_ssc.matricula = form.cleaned_data['matricula']
			new_ssc.semestre = form.cleaned_data['semestre']
			new_ssc.carrera = form.cleaned_data['carrera']
			new_ssc.correo = form.cleaned_data['correo']
			new_ssc.telefono = form.cleaned_data['telefono']
			new_ssc.porque = form.cleaned_data['porque']
			new_ssc.como_te_enteraste = form.cleaned_data['como_te_enteraste']
			new_ssc.comentarios = form.cleaned_data['comentarios']
			new_ssc.para_semestre = form.cleaned_data['para_semestre']
			new_ssc.save()	 

			return HttpResponseRedirect('javascript:{alert("Su informaci&oacute;n ha sido enviada.");}')

	else:
		form = SSCForm()

	return render(request, 'ssc_forma.html', {
		'form': form,
		})



	# if datetime.datetime.now().month>=6:
		# ssc_solicitantes = SSC.objects.filter(fecha__year=datetime.datetime.now().year, para_semestre='ago')
	# else:
		# ssc_solicitantes = SSC.objects.filter(fecha__year=datetime.datetime.now().year, para_semestre='ene')

	# return render_to_response('solicitantes_ssc.html', {
		# 'solicitantes_ssc': ssc_solicitantes
		# }, context_instance=RequestContext(request))

def ssc_crispy_form_vista(request):
	if request.method == 'POST':
		form = SSCForm(request.POST)

		if form.is_valid():
			new_ssc = SSC_inscripcion()
			new_ssc.nombre = form.cleaned_data['nombre']
			new_ssc.matricula = form.cleaned_data['matricula']
			new_ssc.semestre = form.cleaned_data['semestre']
			new_ssc.carrera = form.cleaned_data['carrera']
			new_ssc.correo = form.cleaned_data['correo']
			new_ssc.telefono = form.cleaned_data['telefono']
			new_ssc.porque = form.cleaned_data['porque']
			new_ssc.como_te_enteraste = form.cleaned_data['como_te_enteraste']
			new_ssc.comentarios = form.cleaned_data['comentarios']
			new_ssc.para_semestre = form.cleaned_data['para_semestre']
			new_ssc.save()	 

			return HttpResponseRedirect('javascript:{alert("Su informaci&oacute;n ha sido enviada.");}')

	else:
		form = SSCCrispyForm()

	return render(request, 'ssc_crispy_forma.html', {'form': SSCCrispyForm()})

def ssc_list_vista(request):
	pass

def contacto_vista(request): 
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		
		if form.is_valid():
			send_mail('Contacto GAM Mty', form.cleaned_data['message'], form.cleaned_data['sender'],
    ['gerardo.chapa.q@gmail.com'], fail_silently=False)
			
			return HttpResponseRedirect('javascript:{alert("Su mensaje ha sido enviado.");}')
		
	else:
		form = ContactoForm()

	return render(request, 'contacto.html', {
		'form': form,
		})