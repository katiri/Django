from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.contrib.messages.views import *
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.contrib.auth.mixins import *
from django.contrib.auth.decorators import *

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

def defview(request):
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

class LendoBanco(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('LoginDeUsuario')
    model = Exemplo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Exibição de lista'
        return context

class LendoBancoItem(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('LoginDeUsuario')
    model = Exemplo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Exibição de item'
        return context

class ExemploCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('LoginDeUsuario')
    model = Exemplo
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('LendoBanco')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Criando exemplo'
        return context

class ExemploUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('LoginDeUsuario')
    model = Exemplo
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atualizando exemplo'
        return context

class ExemploDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('LoginDeUsuario')
    permission_required = 'exemplo.delete_exemplo'
    model = Exemplo
    success_url = reverse_lazy('LendoBanco')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Deletando exemplo'
        return context

class CadastroDeUsuario(FormView):
    template_name = 'cadastrouser.html'
    form_class = FormCadastro
    success_url = reverse_lazy('LoginDeUsuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastrando novo usuário'
        return context

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

        perm1 = Permission.objects.get(codename='view_exemplo')
        perm2 = Permission.objects.get(codename='add_exemplo')
        perm3 = Permission.objects.get(codename='change_exemplo')
        # perm4 = Permission.objects.get(codename='delete_exemplo')

        user.user_permissions.add(perm1, perm2, perm3)

        grupo = Group.objects.get(name='Apagadores de exemplos')

        user.groups.add(grupo)

        user.save()

        return super().form_valid(form)

class LoginDeUsuario(FormView):
    template_name = 'login.html'
    form_class = FormLogin

    def get_success_url(self):
        if self.request.GET.get('next'):
            prox = self.request.GET.get('next')
        else:
            prox = '/'

        return str(prox)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login de usuário'
        return context

    def form_valid(self, form):
        nome_usuario = form.cleaned_data['nome_usuario']
        senha = form.cleaned_data['senha']

        user = authenticate(self.request, username=nome_usuario, password=senha)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Nome de usuário ou senha incorretos, favor tentar novamente.')
            return super().form_invalid(form)

@login_required(login_url='LoginDeUsuario')
def logoutdeusuario(request):
    logout(request)
    return redirect('LoginDeUsuario')

class DadosDoUsuario(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('LoginDeUsuario')
    template_name = 'dadosdousuario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Começando um projeto'
        context['dados'] = User.objects.get(id=self.request.user.id)
        # context['dir'] = dir(self.request.user)
        return context

class TrocaDeSenha(LoginRequiredMixin, FormView):
    template_name = 'trocadesenha.html'
    form_class = FormChangeSenha
    success_url = reverse_lazy('DadosDoUsuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Troca de senha do usuário'
        return context

    def form_valid(self, form):
        senha_antiga = form.cleaned_data['senha_antiga']
        senha_nova = form.cleaned_data['senha_nova']
        senha_nova_conf = form.cleaned_data['senha_nova_conf']

        usuario = User.objects.get(id=self.request.user.id)

        senha = authenticate(self.request, username=usuario.username, password=senha_antiga)

        if senha is not None:
            if senha_nova == senha_nova_conf:
                usuario.set_password(senha_nova)
                usuario.save()
                logout(self.request)
                return super().form_valid(form)
            else:
                messages.error(self.request, 'Erro na confirmação da senha nova.')
                return super().form_invalid(form)
        else:
            messages.error(self.request, 'Senha antiga inválida.')
            return super().form_invalid(form)

class LendoCampoRelacionado(ListView):
    model = CamposRelacionado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Exibição de campos relacionados'
        return context

class LendoCampoRelacionadoItem(DetailView):
    model = CamposRelacionado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Exibição de campo relacionado item'
        return context

def consultapersonalizada(request):
    # consultando tudo
    exemplos1 = Exemplo.objects.all()
    # consultando objeto específico
    exemplos2 = Exemplo.objects.get(chave_unica='47d50c1c-59ff-40e1-ab26-2b845abe3a5a')
    # filtrando consulta
    exemplos3 = Exemplo.objects.filter(booleano=True)
    # exemplos3 = Exemplo.objects.filter(frase__exact=teste) # correspondência exata
    # exemplos3 = Exemplo.objects.filter(frase__iexact=Teste) # uma correspondência que não diferencia maiúsculas de minúsculas
    # exemplos3 = Exemplo.objects.filter(frase__contains=est) # teste de contenção
    # exemplos3 = Exemplo.objects.filter(frase__icontains=EsT) # teste de contenção sem distinção entre maiúsculas e minúsculas
    # exemplos3 = Exemplo.objects.filter(frase__startwith=t) # começa com
    # exemplos3 = Exemplo.objects.filter(frase__istartwith=T) # começa com, sem distinção entre maiúsculas e minúsculas
    # exemplos3 = Exemplo.objects.filter(frase__endwith=e) # começa com
    # exemplos3 = Exemplo.objects.filter(frase__iendwith=E) # termina com, sem distinção entre maiúsculas e minúsculas
    # ordenando consulta (para inverter, podemos usar '-inteiro')
    exemplos4 = Exemplo.objects.order_by('inteiro')
    # consultando primeiro item da tabela
    exemplos5 = Exemplo.objects.first()
    # consultando último item da tabela
    exemplos6 = Exemplo.objects.last()
    # contando os objetos
    exemplos7 = Exemplo.objects.count()
    # excluindo determinado item de uma consulta
    exemplos8 = Exemplo.objects.exclude(chave_unica='a73b4c8d-173e-4b8a-92e2-9b19b8c9a18c')
    # limitando resultados de uma consulta
    exemplos9 = Exemplo.objects.all()[:2] # dois primeiros
    # exemplos9 = Exemplo.objects.all()[1:3] # do segundo ao terceiro objeto

    # para mais exemplos consultar documentação https://docs.djangoproject.com/en/3.0/topics/db/queries/


    context = {
        'title': 'Consulta no banco personalizada',
        # 'opções': dir(Exemplo.objects),
        'exemplo1': exemplos1,
        'exemplo2': exemplos2,
        'exemplo3': exemplos3,
        'exemplo4': exemplos4,
        'exemplo5': exemplos5,
        'exemplo6': exemplos6,
        'exemplo7': exemplos7,
        'exemplo8': exemplos8,
        'exemplo9': exemplos9,
    }

    return render(request, 'consultapersonalizada.html', context)