from django.conf.urls import url
from . import views
from mantenimiento.views import IndexContratos



urlpatterns = [
    url(r'^$', IndexContratos.as_view(), name='index'),
    
]