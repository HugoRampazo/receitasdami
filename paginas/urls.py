from django.urls import path
from .views import PaginaInicial, Sobre

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', Sobre.as_view(), name='sobre'),
]