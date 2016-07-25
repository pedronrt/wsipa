from django.contrib import admin

from .models import Contratos, Actividades, TipoActividad


class AdminContratos(admin.ModelAdmin):
    list_display = ['id','numero_contrato', 'fecha_contrato', 'valor_contrato']
    list_display_links = ['numero_contrato']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['numero_contrato', 'fecha_contrato', 'valor_contrato']
    ordering = ['id']

    class Meta:
        model = Contratos


class AdminActividades(admin.ModelAdmin):
    list_display = ['id','predio', 'actividad']
    list_display_links = ['predio']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['cantidad']
    ordering = ['id']

    class Meta:
        model = Actividades

class AdminTipoActividad(admin.ModelAdmin):
    list_display = ['id','nombre']
    list_display_links = ['nombre']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    ordering = ['id']

    class Meta:
        model = TipoActividad

admin.site.register(Contratos, AdminContratos)
admin.site.register(Actividades, AdminActividades)
admin.site.register(TipoActividad, AdminTipoActividad)