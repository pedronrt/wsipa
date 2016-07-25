from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^$', views.IndexPricipal.as_view(),  name='index'),

]

