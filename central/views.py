from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy

class IniciandoDjango(TemplateView):
    template_name = 'django-tutorial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Começando um projeto'
        return context

class ClassView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Aprendendo Django'
        context['texto'] = 'Olá mundo com ClassView'
        context['link'] = 'https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/'
        context['texto_link'] = 'Documentação de Views baseadas em classes'
        return context

def DefView(request):
    context = {
        'title': 'Aprendendo Django',
        'texto': 'Olá mundo com DefView',
        'link': 'https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/',
        'texto_link': 'Documentação de Views baseadas em funções'
    }

    return render(request, 'index.html', context)

class Git(TemplateView):
    template_name = 'git.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Comandos Git'
        return context

class LendoBanco(ListView):
    model = Exemplos
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Exibição de lista'
        return context

class LendoBancoItem(DetailView):
    model = Exemplos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Exibição de item'
        return context

class ExemploCreate(CreateView):
    model = Exemplos
    fields = ['criados',
              'ativo',
              'chave_unica',
              'inteiro',
              'grande_inteiro',
              'pequeno_inteiro',
              'inteiro_positivo',
              'grande_inteiro_positivo',
              'pequeno_inteiro_positivo',
              'num_float',
              'num_decimal',
              'booleano',
              'frase',
              'texto',
              'email',
              'link',
              'slug',
              'data',
              'hora',
              'datahora',
              'duracao',
              'arquivo',
              'caminho_de_arquivo',
              'imagem']
    template_name_suffix = '_create'
    success_url = reverse_lazy('LendoBanco')

class ExemploUpdate(UpdateView):
    model = Exemplos
    fields = ['criados',
              'chave_unica',
              'inteiro',
              'grande_inteiro',
              'pequeno_inteiro',
              'inteiro_positivo',
              'grande_inteiro_positivo',
              'pequeno_inteiro_positivo',
              'num_float',
              'num_decimal',
              'booleano',
              'frase',
              'texto',
              'email',
              'link',
              'slug',
              'data',
              'hora',
              'datahora',
              'duracao',
              'arquivo',
              'caminho_de_arquivo',
              'imagem']
    template_name_suffix = '_update'
    success_url = reverse_lazy('LendoBanco')

class ExemploDelete(DeleteView):
    model = Exemplos
    success_url = reverse_lazy('LendoBanco')