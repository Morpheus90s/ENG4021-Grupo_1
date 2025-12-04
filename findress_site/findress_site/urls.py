from django.contrib import admin
from django.urls import path, include # Certifique-se de que 'include' está importado
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta é a linha principal. 
    # Ela envia todo o tráfego que NÃO for /admin/
    # para o arquivo 'closet.urls' decidir o que fazer.
    path('', include('closet.urls')), 

    # --- ADICIONADO CONFORME O GUIA ---
    # Isso cria automaticamente as rotas de autenticação:
    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ ... e outras
    path('accounts/', include('django.contrib.auth.urls')),
]

# Esta linha é um bônus para o Django mostrar as imagens 
# que você faz upload no /admin
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)