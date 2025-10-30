from django.contrib import admin
from django.urls import path, include # Certifique-se de adicionar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta linha diz ao Django para incluir todas as rotas
    # do arquivo 'closet/urls.py'.
    # O '' significa que ele vai procurar na raiz.
    path('', include('closet.urls')), 
]
