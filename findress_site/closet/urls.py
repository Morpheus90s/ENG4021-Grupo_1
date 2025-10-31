from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta é a linha correta, aponta para o app 'closet'
    path('closet/', include('closet.urls')),
    
    # Esta linha cuida das páginas de login/logout
    path('accounts/', include('django.contrib.auth.urls')),
]