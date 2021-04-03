from django.contrib import admin
from .models import *

@admin.register(Exemplo)
class ExemplosAdmin(admin.ModelAdmin):
    pass

@admin.register(CamposRelacionado)
class CamposRelacionadoAdmin(admin.ModelAdmin):
    pass