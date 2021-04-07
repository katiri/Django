from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IniciandoDjango.as_view(), name='IniciandoDjango'),
    path('class/', ClassView.as_view(), name='ClassIndex'),
    path('lendobanco/', LendoBanco.as_view(), name='LendoBanco'),
    path('lendobancoitem/<slug:slug>/', LendoBancoItem.as_view(), name='LendoBancoItem'),
    path('lendocamposrelacionados/', LendoCampoRelacionado.as_view(), name='LendoCampoRelacionado'),
    path('lendocamposrelacionadositem/<slug:pk>/', LendoCampoRelacionadoItem.as_view(), name='LendoCampoRelacionadoItem'),
    path('criandoexemplo/', ExemploCreate.as_view(), name='ExemploCreate'),
    path('atualizandoexemplo/<slug:slug>/', ExemploUpdate.as_view(), name='ExemploUpdate'),
    path('deletandoexemplo/<slug:slug>/', ExemploDelete.as_view(), name='ExemploDelete'),
    path('cadastrouser/', CadastroDeUsuario.as_view(), name='CadastroDeUsuario'),
    path('loginuser/', LoginDeUsuario.as_view(), name='LoginDeUsuario'),
    path('logoutuser/', logoutdeusuario, name='LogoutDeUsuario'),
    path('dadosdousuario/', DadosDoUsuario.as_view(), name='DadosDoUsuario'),
    path('trocadesenha/', TrocaDeSenha.as_view(), name='TrocaDeSenha'),
    path('consultapersonalizada/', consultapersonalizada, name='ConsultaPersonalizada'),
    path('def/', defview, name='DefIndex'),
    path('git/', Git.as_view(), name='ComandosGit'),
    path('mommy/', criandoExemplos, name='criandoExemplos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)