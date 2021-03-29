from django.contrib import admin
from .models import *

@admin.register(Exemplos)
class ExemplosAdmin(admin.ModelAdmin):
    pass