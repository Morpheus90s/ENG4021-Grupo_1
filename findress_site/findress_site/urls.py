from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 👇 ESTA É A LINHA QUE FALTA! 
    # Ela habilita o sistema de login padrão (que usa a pasta registration/login.html)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # As URLs do seu app Closet
    path('closet/', include('closet.urls')),
    
    # Opcional: Redireciona a página inicial (raiz) direto para o closet
    path('', include('closet.urls')), 
]

# Configuração para servir as fotos (media)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)