import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .validators import valid_extension_pdf
from evaluacion.models import Predios

# modelos de configuracion


class TipoActividad (models.Model):

    nombre = models.CharField("Nombre Municipio", max_length=200, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(TipoActividad, self).save(force_insert, force_update)


# modelos de datos

class Contratos (models.Model):

    def file_path(self, filename):
        ruta = "kml/%s/%s" % (self.id, str(filename))
        return ruta

    numero_contrato=models.IntegerField()
    fecha_contrato=models.DateField()
    valor_contrato=models.DecimalField(max_digits=16,decimal_places=2)
    contratista=models.CharField("Nombres", max_length=200)
    representante=models.CharField("representante", max_length=200)
    nit=models.CharField("nit", max_length=200, null=True, blank=True)
    direccion=models.CharField("direccion", max_length=200, null=True, blank=True)
    tiempo_ejecucion=models.DecimalField(max_digits=4,decimal_places=1)
    fecha_inicio=models.DateField()
    fecha_terminacion=models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero_contrato


    def save(self, force_insert=False, force_update=False):
        self.contratista = self.contratista.upper()
        self.representante = self.representante.upper()
        self.direccion = self.direccion.upper()
        super(Contratos, self).save(force_insert, force_update)


class Actividades (models.Model):

    contrato=models.ForeignKey(Contratos)
    predio=models.ForeignKey(Predios)
    actividad=models.ForeignKey(TipoActividad)
    cantidad=models.DecimalField(max_digits=8,decimal_places=2)
    valor=models.DecimalField(max_digits=16,decimal_places=1)
    tiempo_ejecucion=models.DecimalField(max_digits=4,decimal_places=1)
    fecha_inicio=models.DateField()
    fecha_terminacion=models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.valor

