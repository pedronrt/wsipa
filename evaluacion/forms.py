from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect


from .models import Fotos, Predios

class CrearFotos(CreateView):
    model = Fotos
    template_name = 'evaluacion/nueva-foto.html'
    fields = ['predio','imagen']

    def get_context_data(self, **kwargs):
        context = super(CrearFotos, self).get_context_data(**kwargs)
        context['predio'] = get_object_or_404(Predios, pk__iexact=self.args[0])
        return context









class ActualizarFotos(UpdateView):
    model = Fotos
    fields = ['predio', 'imagen']

class BorrarFotos(DeleteView):
    model = Fotos
    success_url = reverse_lazy('evaluacion:fotos')