from django.shortcuts import render
from django.views.generic import *
from .models import *

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
        return context

def DefView(request):
    context = {
        'title': 'Aprendendo Django',
        'texto': 'Olá mundo com DefView',
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