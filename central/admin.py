from django.contrib import admin
from .models import *

# Documentação para customizar o admin em si https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#adminsite-attributes
admin.AdminSite.site_header = 'Aprendendo Django Admin'
admin.AdminSite.index_title = 'Aprendendo Django Admin 2'

# Documentação do aplicativo de admnistração do Django https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

class CamposRelacionadoInline(admin.TabularInline):
    model = CamposRelacionado
    fk_name = 'chave_estrangeira'

@admin.register(Exemplo)
class ExemplosAdmin(admin.ModelAdmin):
    # Defina date_hierarchycomo o nome de um DateFieldou DateTimeField em seu modelo, e a página da lista de alterações incluirá uma navegação detalhada baseada em data por esse campo.
    date_hierarchy = 'criados'

    # Este atributo, se fornecido, deve ser uma lista de nomes de campos a serem excluídos do formulário.
    # exclude = ['arquivo', 'imagem']

    # o que aparece em campos vazios
    empty_value_display = '-empty-'
    # para um campo em específico
    def view_arquivo(self, obj):
        return obj.arquivo

    view_arquivo.empty_value_display = '???'

    # Use a fields opção de fazer alterações de layout simples nos formulários nas páginas “adicionar” e “alterar”.
    # fields = (
    #     ('criados', 'ativo'),
    #     'chave_unica',
    #     ('inteiro', 'grande_inteiro', 'pequeno_inteiro'),
    #     ('inteiro_positivo', 'grande_inteiro_positivo', 'pequeno_inteiro_positivo'),
    #     ('num_float', 'num_decimal'),
    #     'booleano',
    #     ('frase', 'slug', 'email', 'link'),
    #     'texto',
    #     ('data', 'hora', 'datahora', 'duracao'),
    #     ('arquivo', 'imagem', 'caminho_de_arquivo')
    # )

    # Configure fieldsets para controlar o layout das páginas “adicionar” e “alterar” do administrador.
    fieldsets = (
        (None, {
            'description': 'Campos de controle',
            'fields': (
                ('criados', 'ativo'),
                ('chave_unica', 'booleano'),
            )
        }),
        ('Números', {
            'description': 'Campos de números',
            'classes': ('wide',),
            'fields': (
                ('inteiro', 'grande_inteiro', 'pequeno_inteiro'),
                ('inteiro_positivo', 'grande_inteiro_positivo', 'pequeno_inteiro_positivo'),
                ('num_float', 'num_decimal'),
            )
        }),
        ('Textos', {
            'description': 'Campos de texto',
            # 'classes': ('collapse',),
            'fields': (
                ('frase', 'slug', 'email', 'link', 'selecionar'),
                'texto',
            )
        }),
        ('Datas', {
            'description': 'Campos de data',
            'classes': ('extrapretty',),
            'fields': (
                ('data', 'hora', 'datahora', 'duracao'),
            ),
        }),
        ('Arquivos', {
            'description': 'Campos de upload de arquivos',
            'classes': ('collapse',),
            'fields': (
                ('arquivo', 'imagem', 'caminho_de_arquivo'),
            )
        })
    )

    # Defina list_displaypara controlar quais campos são exibidos na página da lista de alterações do administrador.
    list_display = ('__str__', 'criados', 'ativo', 'modificado')

    # Use list_display_linkspara controlar se e quais campos list_displaydevem ser vinculados à página de “mudança” de um objeto.
    list_display_links = ('__str__', 'criados')

    # Defina list_editablecomo uma lista de nomes de campo no modelo que permitirá a edição na página da lista de alterações.
    list_editable = ('ativo',)

    # Configure list_filterpara ativar os filtros na barra lateral direita da página da lista de alterações do administrador
    list_filter = ('ativo', 'modificado')

    # Defina list_max_show_allpara controlar quantos itens podem aparecer em uma página de lista de alterações de administrador “Mostrar todos”.
    # list_max_show_all = 2

    # Defina list_per_pagepara controlar quantos itens aparecem em cada página da lista de alteração do administrador paginada
    # list_per_page = 1

    # Defina orderingpara especificar como as listas de objetos devem ser ordenadas nas visualizações de administração do Django
    ordering = ('ativo',)

    # Defina prepopulated_fieldscomo um dicionário de mapeamento de nomes de campo para os campos que ele deve preencher previamente
    prepopulated_fields = {
        'slug': ('criados', 'chave_unica')
    }

    # Quaisquer campos nesta opção (que deve ser a listou tuple) exibirão seus dados como estão e não editáveis
    # readonly_fields = ['ativo']

    # Configure save_as para habilitar um recurso “salvar como novo” nos formulários de alteração de administrador.
    save_as = True

    # Quando save_as=True, o redirecionamento padrão após salvar o novo objeto é para a visualização de alteração desse objeto
    save_as_continue = True

    # Defina save_on_toppara adicionar botões de salvar na parte superior de seus formulários de alteração de administrador.
    save_on_top = True

    # Defina view_on_sitepara controlar a exibição ou não do link “Visualizar no local”. Se True (o padrão), o get_absolute_url()
    view_on_site = True

    # css e js personalizados
    # class Media:
    #     css = {
    #         "all": ("my_styles.css",)
    #     }
    #     js = ("my_code.js",)

    # A interface administrativa tem a capacidade de editar modelos na mesma página que um modelo pai. Estes são chamados de inlines.
    inlines = [
        CamposRelacionadoInline
    ]

@admin.register(CamposRelacionado)
class CamposRelacionadoAdmin(admin.ModelAdmin):
    filter_horizontal = ['muitos_para_muitos']
    filter_vertical = ['muitos_para_muitos_self']

    list_display = ('__str__', 'chave_estrangeira')

    # Por padrão, o administrador do Django usa uma interface de caixa de seleção (<select>) para campos que são ForeignKey ou foram
    # choices definidos. Se um campo estiver presente em radio_fields, o Django usará uma interface de botão de rádio ao invés
    radio_fields = {
        'chave_estrangeira': admin.VERTICAL
    }

    # autocomplete_fieldsé uma lista de ForeignKey e/ou ManyToManyField campos que você gostaria de alterar para entradas de
    # preenchimento automático Select2. Você deve definir search_fieldsno objeto relacionado ModelAdminporque a pesquisa de
    # preenchimento automático o utiliza.
    # search_fields = ['chave_estrangeira']
    # autocomplete_fields = ['chave_estrangeira_self']

    # raw_id_fieldsé uma lista de campos que você gostaria de transformar em um Inputwidget para um ForeignKey ou ManyToManyField
    # raw_id_fields = ('chave_estrangeira_self',)

