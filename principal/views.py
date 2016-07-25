from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import UserLoginForm


class IndexPricipal(generic.TemplateView):
    template_name = 'principal/index.html'

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect ('/')

    return render(request,"principal/login.html", {"form":form})


def logout_view(request):
    logout(request)
    return render(request,"principal/index.html", {})