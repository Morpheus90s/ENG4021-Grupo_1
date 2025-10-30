# findress_site/urls.py

from django.contrib import admin
from django.urls import path, include # Adicione 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('closet.urls')), # <-- ADICIONE ESTA LINHA
]