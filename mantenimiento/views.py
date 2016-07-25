from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from .models import Contratos

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexContratos(ListView):
    model = Contratos
    template_name = 'mantenimiento/index.html'
    context_object_name = 'lista_contratos'