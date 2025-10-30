# Em findress_site/closet/admin.py

from django.contrib import admin
from .models import PecaRoupa, Look, Gostar, LookPeca # Importe seus modelos

# Registra os modelos para que apareçam na interface de admin
admin.site.register(PecaRoupa)
admin.site.register(Look)
admin.site.register(Gostar)
admin.site.register(LookPeca)