from django.contrib import admin
from .models import (
    Municipios, Veredas, TipoTitularidad, TipoImpedimento, Lonja,
    Subzona, Microcuenca, Acueducto,  EstadoPredio, Despacho_notarial, Prestador, NivelAcueducto)


class AdminMunicipios(admin.ModelAdmin):
    list_display = ["id","nombre"]
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre']
    ordering = ['id']

    class Meta:
        model = Municipios



class AdminVeredas(admin.ModelAdmin):
    list_display = ["id","nombre", "municipios_id"]
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre']
    ordering = ['id']

    class Meta:
        model = Veredas

class AdminEstado(admin.ModelAdmin):
    list_display = ["id","nombre"]
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre']
    ordering = ['id']

    class Meta:
        model = EstadoPredio

class AdminDespachoNotarial(admin.ModelAdmin):
    list_display = ["id","nombre"]
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre']
    ordering = ['id']

    class Meta:
        model = Despacho_notarial

class AdminSubzona(admin.ModelAdmin):
    list_display = ["id","nombre", "codigo"]
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre']
    ordering = ['id']

    class Meta:
        model = Subzona

class AdminMicrocuenca(admin.ModelAdmin):
    list_display = ["id","nombre", "subzona"]
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre']
    ordering = ['id']

    class Meta:
        model = Microcuenca

class AdminAcueducto(admin.ModelAdmin):
    list_display = ["id","nombre"]
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre']
    ordering = ['id']

    class Meta:
        model = Acueducto

class AdminPrestador(admin.ModelAdmin):
    list_display = ["id","nombre"]
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre']
    ordering = ['id']

    class Meta:
        model = Prestador

class AdminNivelAcueducto(admin.ModelAdmin):
    list_display = ["id","nombre"]
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre']
    ordering = ['id']

    class Meta:
        model = NivelAcueducto



admin.site.register(Municipios, AdminMunicipios)
admin.site.register(Veredas, AdminVeredas)
admin.site.register(TipoTitularidad)
admin.site.register(TipoImpedimento)
admin.site.register(Lonja)
admin.site.register(Microcuenca, AdminMicrocuenca)
admin.site.register(Subzona, AdminSubzona)
admin.site.register(Acueducto, AdminAcueducto)
admin.site.register(EstadoPredio, AdminEstado)
admin.site.register(Despacho_notarial, AdminDespachoNotarial)
admin.site.register(Prestador, AdminPrestador)
admin.site.register(NivelAcueducto, AdminNivelAcueducto)


