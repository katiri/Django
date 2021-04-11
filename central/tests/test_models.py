from django.test import TestCase
from central.models import *
from model_mommy import mommy

class TestExemplo(TestCase):
    def setUp(self):
        self.ex = mommy.make(Exemplo)

    def test_str(self):
        # testando se são iguais
        self.assertEqual(str(self.ex), 'Exemplo ['+str(self.ex.chave_unica)+']')

    def test_get_absolute_url(self):
        self.assertEqual(str(self.ex.get_absolute_url()), '/lendobancoitem/'+str(self.ex.chave_unica)+'/')

class TestCamposRelacionado(TestCase):
    def setUp(self):
        self.campo = mommy.make(CamposRelacionado)

    def test_str(self):
        # testando se são iguais
        self.assertEqual(str(self.campo), 'Chave estrangeira: ' + str(self.campo.chave_estrangeira))

class TestUsuarioManager(TestCase):
    def setUp(self):
        self.email = 'teste@email.com'
        self.password = 'Test123456'
        self.extra_fields = {'is_superuser': True, 'is_staff': False}

    def test_create_user(self):
        self.assertTrue(CustomUsuario.objects.create_user(self.email, self.password))

    def test_create_superuser(self):
        self.assertTrue(CustomUsuario.objects.create_superuser(self.email, self.password))

        with self.assertRaisesMessage(ValueError, 'Superuser precisa ter is_superuser=True'):
            CustomUsuario.objects.create_superuser(self.email, self.password, is_superuser=False)

        with self.assertRaisesMessage(ValueError, 'Superuser precisa ter is_staff=True'):
            CustomUsuario.objects.create_superuser(self.email, self.password, is_staff=False)

    def test_not_email(self):
        with self.assertRaisesMessage(ValueError, 'O e-mail é obrigatório'):
            CustomUsuario.objects.create_user(False)

class TestCustomUsuario(TestCase):
    def setUp(self):
        self.user = mommy.make(CustomUsuario)

    def test_str(self):
        self.assertEqual(str(self.user), str(self.user.email))