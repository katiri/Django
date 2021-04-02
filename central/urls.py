from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IniciandoDjango.as_view(), name='IniciandoDjango'),
    path('class/', ClassView.as_view(), name='ClassIndex'),
    path('lendobanco/', LendoBanco.as_view(), name='LendoBanco'),
    path('lendobancoitem/<slug:slug>/', LendoBancoItem.as_view(), name='LendoBancoItem'),
    path('criandoexemplo/', ExemploCreate.as_view(), name='ExemploCreate'),
    path('atualizandoexemplo/<slug:slug>/', ExemploUpdate.as_view(), name='ExemploUpdate'),
    path('deletandoexemplo/<slug:slug>/', ExemploDelete.as_view(), name='ExemploDelete'),
    path('cadastrouser/', CadastroDeUsuario.as_view(), name='CadastroDeUsuario'),
    path('def/', DefView, name='DefIndex'),
    path('git/', Git.as_view(), name='ComandosGit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)