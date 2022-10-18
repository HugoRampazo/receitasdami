from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

class Sobre(TemplateView):
    template_name = 'paginas/sobre.html'