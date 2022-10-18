from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from post import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('paginas.urls')),
    path('', include('post.urls')),
    path('', include('usuarios.urls')),
    path('receita/<int:receita_id>/', views.receita),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)