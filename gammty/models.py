from django.db import models
from datetime import date

class Nosotros(models.Model):
	mision = models.CharField(max_length=255)
	vision_anho = models.DecimalField(max_digits=4, decimal_places=0)
	vision_texto = models.CharField(max_length=255)
	valores = models.CharField(max_length=200)

	def __unicode__(self):
		return self.mision

	def valores_lista(self):
		return self.valores.split(',')


class Objetivo(models.Model):
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	descripcion = models.CharField(max_length=255)
	nosotros = models.ForeignKey('Nosotros')
	
	def __unicode__(self):
		return self.descripcion

class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nombre

class Servicio(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=255)
	tipo = models.ForeignKey('Tipo')

	def __unicode__(self):
		return self.nombre

class Tipo(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class SSC_inscripcion(models.Model):
	nombre = models.CharField(max_length=100)
	matricula = models.CharField(max_length=10)
	semestre = models.IntegerField()
	carrera = models.CharField(max_length=5)
	correo = models.EmailField(max_length=100)
	telefono = models.CharField(max_length=20)
	porque = models.CharField(max_length=255)
	como_te_enteraste = models.CharField(max_length=255)
	comentarios = models.CharField(max_length=255)
	fecha = models.DateField(auto_now_add=True)
	para_semestre = models.CharField(max_length=7)

	def __unicode__(self):
		return self.matricula