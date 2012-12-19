#encoding:utf-8
from django import forms

from gammty.models import SSC_inscripcion

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions

class SSCCrispyForm(forms.Form):
	nombre = forms.CharField(label="Nombre")
	matricula = forms.CharField(label="Matrícula")
	semestre = forms.IntegerField(label="Semestre")
	carrera = forms.CharField(label="Carrera")
	correo = forms.EmailField(label="Correo")
	telefono = forms.CharField(label="Teléfono")
	porque = forms.CharField(widget=forms.Textarea, label="¿Porqué te gustaría formar parte del servicio?")
	como_te_enteraste = forms.CharField(widget=forms.Textarea, label="¿Cómo te enteraste de nosotros?")
	comentarios = forms.CharField(widget=forms.Textarea, label="Comentarios adicionales")
	PARA_SEMESTRE_CHOICES = (('Ago-Dic', 'Ago-Dic'), 
		('Ene-Feb', 'Ene-Feb'))
	para_semestre = forms.ChoiceField(widget=forms.Select, choices=PARA_SEMESTRE_CHOICES, label="Semestre")

	# Uni-form
	helper = FormHelper()
	helper.form_class = 'form-horizontal'
	helper.layout = Layout(
        Field('nombre', css_class='input-xlarge'),
        Field('matricula', css_class='input-xlarge'),
        Field('semestre', css_class='input-xlarge'),
        Field('carrera', css_class='input-xlarge'),
        Field('correo', css_class='input-xlarge'),
        Field('telefono', css_class='input-xlarge'),
        Field('porque', rows="3", css_class='input-xlarge'),
        Field('como_te_enteraste', css_class='input-xlarge'),
        Field('comentarios', rows="3", css_class='input-xlarge'),
        'para_semestre',
        FormActions(
            Submit('submit', 'Enviar', css_class="btn-primary"),
        )
    )

class ContactoForm(forms.Form):
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()

class SSCForm(forms.Form):
	nombre = forms.CharField()
	matricula = forms.CharField()
	semestre = forms.IntegerField()
	carrera = forms.CharField()
	correo = forms.EmailField()
	telefono = forms.CharField()
	porque = forms.CharField(widget=forms.Textarea)
	como_te_enteraste = forms.CharField(widget=forms.Textarea)
	comentarios = forms.CharField(widget=forms.Textarea)
	PARA_SEMESTRE_CHOICES = (('Ago-Dic', 'Ago-Dic'), 
		('Ene-Feb', 'Ene-Feb'))
	para_semestre = forms.ChoiceField(widget=forms.Select, choices=PARA_SEMESTRE_CHOICES)