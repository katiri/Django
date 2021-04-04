from django.contrib import admin
from .models import *

# Documentação do aplicativo de admnistração do Django https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

@admin.register(Exemplo)
class ExemplosAdmin(admin.ModelAdmin):
    # Ordenação na lista
    # date_hierarchy = 'criados'

    # Este atributo, se fornecido, deve ser uma lista de nomes de campos a serem excluídos do formulário.
    # exclude = ['arquivo', 'imagem']

    # Use a fieldsopção de fazer alterações de layout simples nos formulários nas páginas “adicionar” e “alterar”.
    fields = (
        ('criados', 'ativo'),
        'chave_unica',
        ('inteiro', 'grande_inteiro', 'pequeno_inteiro'),
        ('inteiro_positivo', 'grande_inteiro_positivo', 'pequeno_inteiro_positivo'),
        ('num_float', 'num_decimal'),
        'booleano',
        ('frase', 'slug', 'email', 'link'),
        'texto',
        ('data', 'hora', 'datahora', 'duracao'),
        ('arquivo', 'imagem', 'caminho_de_arquivo')
    )

    # Outras configurações na documentação https://docs.djangoproject.com/en/3.0/ref/contrib/admin/


@admin.register(CamposRelacionado)
class CamposRelacionadoAdmin(admin.ModelAdmin):
    pass