from django.test import TestCase, Client
from central.views import *

class TestIniciandoDjango(TestCase):
    def setUp(self):
        self.request = IniciandoDjango()
        self.context = {
            'view': self.request,
            'title': 'Começando um projeto',
        }

    def test_get_context_data(self):
        self.assertEqual(self.request.get_context_data(), self.context)

class TestClassView(TestCase):
    def setUp(self):
        self.request = ClassView()
        self.context = {
            'view': self.request,
            'title': 'Aprendendo Django',
            'texto': 'Olá mundo com ClassView',
            'link': 'https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/',
            'texto_link': 'Documentação de Views baseadas em classes',
        }

    def test_get_context_data(self):
        self.assertEqual(self.request.get_context_data(), self.context)

class TestDefView(TestCase):
    def setUp(self):
        self.context = {
            'title': 'Aprendendo Django',
            'texto': 'Olá mundo com DefView',
            'link': 'https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/',
            'texto_link': 'Documentação de Views baseadas em funções',
        }
        self.user = Client()

    def test_requisicao(self):
        request = self.user.get(reverse_lazy('DefIndex'))
        self.assertEquals(request.status_code, 200)

class TestGit(TestCase):
    def setUp(self):
        self.request = Git()
        self.context = {
            'view': self.request,
            'title': 'Comandos Git',
        }

    def test_get_context_data(self):
        self.assertEqual(self.request.get_context_data(), self.context)