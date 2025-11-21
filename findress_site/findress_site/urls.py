# Este é o conteúdo CORRETO para findress_site/findress_site/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("closet/", include("closet.urls")),      # <-- Inclui o arquivo do Passo 1
    path("usuario/", include("usuario.urls")),   # (se você já o criou)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # NÃO PODE ter outra linha "path('closet/', ...)" aqui!
]