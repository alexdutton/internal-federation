from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from . import forms
from . import models


class IndexView(ListView):
    template_name = 'infed/index.html'
    model = models.ServiceProvider


class ServiceProviderCreateView(CreateView):
    model = models.ServiceProvider
    form_class = forms.ServiceProviderForm


class ServiceProviderDetailView(DetailView):
    model = models.ServiceProvider



class ServiceProviderUpdateView(UpdateView):
    model = models.ServiceProvider
    form_class = forms.ServiceProviderForm


