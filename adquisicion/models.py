from django.db import models
from evaluacion.models import Predios
from configuracion.models import Despacho_notarial


# Create your models here.

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .validators import valid_extension_pdf



# Create your models here.

class Contratos (models.Model):

    def file_path(self, filename):
        ruta = "kml/%s/%s" % (self.id, str(filename))
        return ruta

    numero_contrato=models.IntegerField()
    fecha_contrato=models.DateField()
    valor_contrato=models.DecimalField(max_digits=16,decimal_places=2)
    nombre_vendedor=models.CharField("Nombres", max_length=200)
    apellido1_vendedor=models.CharField("Primer Apellido", max_length=200)
    apellido2_vendedor=models.CharField("Segundo Apellido", max_length=200, null=True, blank=True)
    identificacion_vendedor=models.IntegerField()
    direccion_vendedor=models.CharField("direccion", max_length=200, null=True, blank=True)
    predio=models.ForeignKey(Predios)
    numero_escritura=models.IntegerField()
    fecha_escritura=models.DateField()
    despacho_notarial=models.ForeignKey(Despacho_notarial)
    folio_matricula=models.CharField("Folio Matricula inmobiliaria", max_length=12, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_vendedor


    def save(self, force_insert=False, force_update=False):
        self.nombre_vendedor = self.nombre_vendedor.upper()
        self.apellido1_vendedor = self.apellido1_vendedor.upper()
        self.apellido2_vendedor = self.apellido2_vendedor.upper()
        self.direccion_vendedor = self.direccion_vendedor.upper()
        super(Contratos, self).save(force_insert, force_update)
