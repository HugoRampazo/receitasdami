from django.urls import path
from .views import ReceitaCreate, ReceitaDelete, ReceitaList, ReceitaUpdate

urlpatterns = [
    # Receita
    path('cadastrar/receita/', ReceitaCreate.as_view(), name='cadastrar-receita'),
    path('editar/receita/<int:pk>/', ReceitaUpdate.as_view(), name='editar-receita'),
    path('excluir/receita/<int:pk>/', ReceitaDelete.as_view(), name='excluir-receita'),
    path('listar/receitas/', ReceitaList, name='listar-receitas'),
    
]