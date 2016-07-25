from django.conf.urls import url
from . import views
from evaluacion.views import IndexPredios, DetallePredios, FotosPredios, MapasPredios
from .forms import CrearFotos, ActualizarFotos, BorrarFotos


urlpatterns = [
    url(r'^$', IndexPredios.as_view(), name='index'),
    url(r'^detalle/([\w-]+)/$', DetallePredios.as_view(), name="detalle"),
    url(r'^detalle/fotos/([\w-]+)/$', FotosPredios.as_view(), name="fotos"),
    url(r'^detalle/mapas/([\w-]+)/$', MapasPredios.as_view(), name="mapas"),

    url(r'foto/agregar/([\w-]+)$', CrearFotos.as_view(), name='agregar­fotos'),


    url(r'foto/(?P<pk>[0­9]+)/$', ActualizarFotos.as_view(), name='actualizar­fotos'),
    url(r'foto/(?P<pk>[0­9]+)/borrar/$', BorrarFotos.as_view(), name='borrar­fotos'),
]