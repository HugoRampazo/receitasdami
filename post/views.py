from django.shortcuts import render, get_object_or_404
from .models import Receita
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator


################# RECEITAS ################

# Essa classe serve para criar uma receita.
class ReceitaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model=Receita
    fields=['titulo', 'categoria', 'imagem', 'publicada', 'tempo_preparo', 'rende_ate', 'ingredientes', 'modo_de_preparo']
    template_name = 'post/form.html'
    success_url = reverse_lazy('listar-receitas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar nova receita"
        context['botao'] = "Cadastrar"
        return context


# Essa classe serve para editar uma receita específica.
class ReceitaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model=Receita
    fields=['titulo', 'categoria', 'imagem', 'publicada', 'tempo_preparo', 'rende_ate', 'ingredientes', 'modo_de_preparo']
    template_name = 'post/form-update.html'
    success_url = reverse_lazy('listar-receitas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar receita"
        context['botao'] = "Salvar"
        return context


# Essa classe serve para excluir uma receita específica.
class ReceitaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model=Receita
    template_name = 'post/form-excluir.html'
    success_url = reverse_lazy('listar-receitas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Excluir receita"
        context['botao'] = "Excluir"
        return context


# Essa função serve para visualizar e filtrar todas as receitas.
def ReceitaList(request):
    receitas = Receita.objects.filter(publicada=True)
    
    if 'procurar' in request.GET and request.GET['procurar']:
        receitas = receitas.filter(Q(categoria__icontains=request.GET['procurar']) | Q(titulo__icontains=request.GET['procurar']))
    
    receitas   = receitas.order_by('-id')

    paginator = Paginator(receitas, 12)

    page = request.GET.get('page')

    receitas = paginator.get_page(page)

    return render(request, 'post/listas/lista-receitas.html', {'receitas': receitas})


# Essa função serve para visualizar uma receita específica.
def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    return render(request, 'post/listas/receitas.html', {'receita':receita})