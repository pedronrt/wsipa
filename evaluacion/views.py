from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, FormView, CreateView, TemplateView
from .models import Predios, Ofertas, Avaluos, Titularidad, Topografia, Caracterizacion, Fotos

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexPredios(ListView):
    queryset = Predios.objects.all().order_by('-id')
    template_name = 'evaluacion/index.html'
    context_object_name = 'lista_predios'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(IndexPredios, self).get_context_data(**kwargs)
        if 'q' in self.request.GET and self.request.GET['q']:
            busca = self.request.GET['q'].upper()
            context['lista_predios'] = Predios.objects.filter(Q(nombre__contains=busca) | Q(matricula__contains=busca))
        return context





class DetallePredios(ListView):
    model = Ofertas
    template_name = 'evaluacion/detalle.html'
    context_object_name = 'lista_ofertas'

    def get_queryset(self):
        self.predio = get_object_or_404(Predios, pk__iexact=self.args[0])
        return Ofertas.objects.filter(predio=self.predio)

    def get_context_data(self, **kwargs):
        context = super(DetallePredios, self).get_context_data(**kwargs)
        context['predio'] = self.predio
        context['lista_titularidad'] = Titularidad.objects.filter(predio=self.predio)
        context['lista_topografias'] = Topografia.objects.filter(predio=self.predio)
        context['lista_caracterizaciones'] = Caracterizacion.objects.filter(predio=self.predio)
        context['lista_avaluos'] = Avaluos.objects.filter(predio=self.predio)
        return context


class FotosPredios(ListView):
    model = Fotos
    template_name = 'evaluacion/fotos.html'
    context_object_name = 'lista_fotos'

    def get_queryset(self):
        self.predio = get_object_or_404(Predios, pk__iexact=self.args[0])
        return Fotos.objects.filter(predio=self.predio)

    def get_context_data(self, **kwargs):
        context = super(FotosPredios, self).get_context_data(**kwargs)
        context['predio'] = self.predio
        return context



class MapasPredios(ListView):
    model = Predios
    template_name = 'evaluacion/mapas.html'
    context_object_name = 'lista_coordenadas'

    def get_queryset(self):
        self.predio = get_object_or_404(Predios, pk__iexact=self.args[0])
        return Predios.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MapasPredios, self).get_context_data(**kwargs)
        context['predio'] = self.predio
        return context




