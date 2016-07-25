from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .validators import valid_extension_pdf, valid_extension_kml

from configuracion.models import Municipios, Veredas, TipoTitularidad, TipoImpedimento, Lonja, EstadoPredio, Subzona, Microcuenca, Acueducto

# Create your models here.

class Predios (models.Model):

    def file_path(self, filename):
        ruta = "kml/%s/%s" % (self.id, str(filename))
        return ruta

    nombre=models.CharField("Nombre del Predio", max_length=200)
    matricula = models.CharField("Folio Matricula inmobiliaria", max_length=12, unique=True)
    municipio = models.ForeignKey(Municipios)
    vereda = models.ForeignKey(Veredas)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    estado = models.ForeignKey(EstadoPredio, default=1)
    kml=models.FileField(upload_to=file_path, null=True, blank=True, validators=[valid_extension_kml])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Predios, self).save(force_insert, force_update)

class Ofertas(models.Model):

    def file_path(self, filename):
        ruta = "documentos/%s/%s" % (self.predio.id, str(filename))
        return ruta

    predio = models.ForeignKey(Predios)
    nombres = models.CharField("Nombres", max_length=50)
    apellido1 = models.CharField("Primer Apellido", max_length=32)
    apellido2 = models.CharField("Segundo Apellido", max_length=32, null=True, blank=True)
    cedula = models.IntegerField()
    direccion = models.CharField("Direccion", max_length=124, null=True, blank=True)
    municipio = models.ForeignKey(Municipios)
    telefono = models.CharField("Telefono", max_length=24, null=True, blank=True)
    documento = models.FileField(upload_to=file_path, null=True, blank=True, validators=[valid_extension_pdf])
    fecha_oferta = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombres

    def save(self, force_insert=False, force_update=False):
        self.nombres = self.nombres.upper()
        self.apellido1 = self.apellido1.upper()
        self.apellido2 = self.apellido2.upper()
        self.direccion = self.direccion.upper()
        super(Ofertas, self).save(force_insert, force_update)

class Titularidad(models.Model):

    def file_path(self, filename):
        ruta = "documentos/%s/%s" % (self.predio.id, str(filename))
        return ruta

    predio = models.ForeignKey(Predios)
    tipo_documento = models.ForeignKey(TipoTitularidad)
    numero = models.CharField("Número",max_length=10)
    fecha_documento = models.DateField(null=True, blank=True)
    tipo_impedimento = models.ForeignKey(TipoImpedimento, default=1)
    documento = models.FileField(upload_to=file_path, null=True, blank=True, validators=[valid_extension_pdf])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero

    def save(self, force_insert=False, force_update=False):
        self.numero = self.numero.upper()
        super(Titularidad, self).save(force_insert, force_update)

class Topografia(models.Model):

    def file_path(self, filename):
        ruta = "documentos/%s/%s" % (self.predio.id, str(filename))
        return ruta

    predio = models.ForeignKey(Predios)
    fecha_topografia = models.DateField()
    area_total = models.DecimalField(max_digits=11,decimal_places=4)
    area_bosque = models.DecimalField(max_digits=11, decimal_places=4, null=True, blank=True)
    area_sabana = models.DecimalField(max_digits=11, decimal_places=4, null=True, blank=True)
    area_agricola = models.DecimalField(max_digits=11, decimal_places=4, null=True, blank=True)
    documento = models.FileField(upload_to=file_path, null=True, blank=True, validators=[valid_extension_pdf])
    plano = models.FileField(upload_to=file_path, null=True, blank=True, validators=[valid_extension_pdf])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)



class Caracterizacion(models.Model):

    def file_path(self, filename):
        ruta = "documentos/%s/%s" % (self.predio.id, str(filename))
        return ruta

    predio = models.ForeignKey(Predios)
    fecha_caracterizacion = models.DateField()
    subzona=models.ForeignKey(Subzona)
    microcuenca=models.ForeignKey(Microcuenca)
    acueducto=models.ForeignKey(Acueducto)
    documento = models.FileField(upload_to=file_path, null=True, blank=True, validators=[valid_extension_pdf])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)





class Avaluos(models.Model):

    def file_path(self, filename):
        ruta = "documentos/%s/%s" % (self.predio.id, str(filename))
        return ruta

    predio = models.ForeignKey(Predios)
    fecha_avaluo = models.DateField()
    valor_total = models.DecimalField(max_digits=12,decimal_places=2)
    valor_hectarea = models.DecimalField(max_digits=12,decimal_places=2)
    lonja = models.ForeignKey(Lonja)
    documento = models.FileField(upload_to=file_path, null=True, blank=True, validators=[valid_extension_pdf])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


class Fotos(models.Model):

    def imagen_path(self, filename):
        ruta = "fotos/%s/%s" % (self.predio.id,  str(filename))
        return ruta

    predio = models.ForeignKey(Predios)
    imagen = models.ImageField(upload_to=imagen_path, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)



    def get_absolute_url(self):
        return reverse('evaluacion:fotos', args=[str(self.predio_id)])
