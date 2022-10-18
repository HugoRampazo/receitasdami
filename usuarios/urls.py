from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'usuarios/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # registrar usuario
    path('criar-contra/', UsuarioCreate.as_view(), name='criar-conta'),
]