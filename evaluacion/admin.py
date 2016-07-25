from django.contrib import admin

from .models import Predios, Ofertas, Titularidad, Topografia, Caracterizacion, Avaluos, Fotos


class AdminPredios(admin.ModelAdmin):
    list_display = ['id','nombre', 'matricula', 'municipio']
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['nombre', 'matricula']
    ordering = ['id']

    class Meta:
        model = Predios


class AdminOferta(admin.ModelAdmin):
    list_display = ['id', 'predio','nombres','apellido1','apellido2','documento' ]
    list_display_links = ['nombres']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['predio','nombres','apellido1','apellido2','documento']
    ordering = ['id']

    class Meta:
        model = Ofertas


class AdminTitularidad(admin.ModelAdmin):
    list_display = ['id','predio', 'tipo_documento', 'numero', 'fecha_documento']
    list_display_links = ['predio']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['predio', 'tipo_documento']
    ordering = ['id']

    class Meta:
        model = Titularidad


class AdminTopografia(admin.ModelAdmin):
    list_display = ['id', 'predio', 'fecha_topografia', 'area_total','area_bosque','area_sabana','area_agricola' ]
    list_display_links = ['predio']
    list_filter = ['fecha_registro', 'fecha_modificacion', 'area_total']
    search_fields = ['predio']
    ordering = ['id']

    class Meta:
        model = Topografia



class AdminAvaluos(admin.ModelAdmin):
    list_display = ['id','predio', 'fecha_avaluo', 'valor_total','lonja']
    list_display_links = ['predio']
    list_filter = ['valor_total', 'fecha_registro', 'fecha_modificacion' ]
    search_fields = ['predio', 'lonja']
    ordering = ['id']

    class Meta:
        model = Avaluos


class AdminFotos(admin.ModelAdmin):
    list_display = ['predio', 'imagen']
    list_display_links = ['predio']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['predio']
    ordering = ['id']

    class Meta:
        model = Fotos

class AdminCaracterizacion(admin.ModelAdmin):
    list_display = ['predio', 'fecha_caracterizacion', 'subzona', 'microcuenca', 'acueducto', 'documento']
    list_display_links = ['predio']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['predio']
    ordering = ['id']

    class Meta:
        model = Caracterizacion

admin.site.register(Predios, AdminPredios)
admin.site.register(Ofertas, AdminOferta)
admin.site.register(Titularidad, AdminTitularidad)
admin.site.register(Topografia, AdminTopografia)
admin.site.register(Caracterizacion, AdminCaracterizacion)
admin.site.register(Avaluos, AdminAvaluos)
admin.site.register(Fotos, AdminFotos)