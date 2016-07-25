from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, FormView, CreateView, TemplateView
from django.views.generic.detail import SingleObjectMixin



from adquisicion.models import Contratos

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexContratos(ListView):
    template_name = 'adquisicion/index.html'
    paginate_by = 5
    queryset = Contratos.objects.all().order_by('-id')
    context_object_name = 'lista_contratos'


    def get_context_data(self, **kwargs):
        context = super(IndexContratos, self).get_context_data(**kwargs)
        if 'q' in self.request.GET and self.request.GET['q']:
            busca = self.request.GET['q'].upper()
            context['lista_contratos'] = Contratos.objects.filter(numero_contrato__contains=busca)

        return context










