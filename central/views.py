from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.models import *

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

class CadastroDeUsuario(FormView):
    template_name = 'cadastrouser.html'
    form_class = FormCadastro
    success_url = '/admin/'

    def form_valid(self, form):
        nome_usuario = form.cleaned_data['nome_usuario']
        senha = form.cleaned_data['senha']
        email = form.cleaned_data['email']
        primeiro_nome = form.cleaned_data['primeiro_nome']
        ultimo_nome = form.cleaned_data['ultimo_nome']

        user = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        user.first_name = primeiro_nome
        user.last_name = ultimo_nome
        user.is_staff = True

        perm1 = Permission.objects.get(codename='view_exemplos')
        perm2 = Permission.objects.get(codename='add_exemplos')
        perm3 = Permission.objects.get(codename='change_exemplos')
        # perm4 = Permission.objects.get(codename='delete_exemplos')

        user.user_permissions.add(perm1, perm2, perm3)

        grupo = Group.objects.get(name='Grupo1')

        user.groups.add(grupo)

        user.save()

        return super().form_valid(form)