from django.contrib import admin

from .models import Contratos


class AdminContratos(admin.ModelAdmin):
    list_display = ['id','numero_contrato', 'fecha_contrato', 'valor_contrato', 'nombre_vendedor', 'apellido1_vendedor', 'predio']
    list_display_links = ['numero_contrato']
    list_filter = ['fecha_registro', 'fecha_modificacion']
    search_fields = ['numero_contrato', 'fecha_contrato', 'valor_contrato', 'nombre_vendedor', 'apellido1_vendedor', 'folio_matricula']
    ordering = ['id']

    class Meta:
        model = Contratos

admin.site.register(Contratos, AdminContratos)