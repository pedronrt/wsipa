import datetime

from django.db import models
from django.conf import settings
from django.core.validators import ValidationError


class Municipios(models.Model):
    nombre = models.CharField("Nombre Municipio", max_length=200, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Municipios, self).save(force_insert, force_update)

class Veredas(models.Model):
    municipios=models.ForeignKey(Municipios)
    nombre = models.CharField("Nombre Vereda", max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Veredas, self).save(force_insert, force_update)

class TipoTitularidad(models.Model):
    nombre = models.CharField("Tipo de Titularidad", max_length=32)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(TipoTitularidad, self).save(force_insert, force_update)

class TipoImpedimento(models.Model):
    nombre = models.CharField("Tipo de Impedimento", max_length=64)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(TipoImpedimento, self).save(force_insert, force_update)



class Lonja(models.Model):
    nombre = models.CharField("Lonja Inmobiliaria", max_length=64)
    direccion = models.CharField("Direccion", max_length=128)
    municipio = models.ForeignKey(Municipios)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.direccion = self.direccion.upper()
        super(Lonja, self).save(force_insert, force_update)


class EstadoPredio(models.Model):
    nombre = models.CharField("Estados", max_length=64)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(EstadoPredio, self).save(force_insert, force_update)


class Despacho_notarial(models.Model):
    nombre = models.CharField("Despacho Notarial", max_length=124)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Despacho_notarial, self).save(force_insert, force_update)

# *** modulo de evaluacion ***


class Subzona(models.Model):
    nombre = models.CharField("Subzona Hidrografica", max_length=64)
    codigo = models.IntegerField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Subzona, self).save(force_insert, force_update)

class Microcuenca(models.Model):
    subzona = models.ForeignKey(Subzona)
    nombre = models.CharField("Nombre de la microcuenca", max_length=64)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Microcuenca, self).save(force_insert, force_update)

class Prestador(models.Model):
    nombre = models.CharField("Prestador del Servicio de Acueducto", max_length=124)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Prestador, self).save(force_insert, force_update)

class NivelAcueducto(models.Model):
    nombre=models.CharField("Nivel Acueducto", max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(NivelAcueducto, self).save(force_insert, force_update)


class Acueducto(models.Model):
    nombre=models.CharField("Nombre del Acueducto", max_length=200)
    usuarios=models.IntegerField()
    prestador=models.ForeignKey(Prestador)
    nivel=models.ForeignKey(NivelAcueducto)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(Acueducto, self).save(force_insert, force_update)

