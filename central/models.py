import uuid
from django.db import models

# documentação para campos https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

class Base(models.Model):
    criados = models.DateField('Criação')
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Exemplos(Base):
    # Gera um id para cada linha
    # auto_campo = models.AutoField()
    # Id maior
    # grande_auto_campo = models.BigAutoField()
    # Como um AutoField, mas só permite valores sob um certo limite (dependente do banco de dados).
    # pequeno_auto_campo = models.SmallAutoField()

    # Um campo para armazenar identificadores exclusivos universalmente. Usa a UUIDclasse Python. requer import uuid
    chave_unica = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)

    # Campo de número
    inteiro = models.IntegerField()
    # Campo de número grande
    grande_inteiro = models.BigIntegerField()
    # Como um IntegerField, mas só permite valores em um determinado ponto (dependente do banco de dados)
    pequeno_inteiro = models.SmallIntegerField()
    # Como um IntegerField, mas deve ser positivo ou zero ( 0)
    inteiro_positivo = models.PositiveIntegerField()
    # Como um BigIntegerField, mas deve ser positivo ou zero ( 0)
    grande_inteiro_positivo = models.PositiveBigIntegerField()
    # Como um SmallIntegerField, mas deve ser positivo ou zero ( 0)
    pequeno_inteiro_positivo = models.PositiveSmallIntegerField()
    # Um número de ponto flutuante representado em Python por uma floatinstância.
    num_float = models.FloatField()
    # Um número decimal de precisão fixa, representado em Python por uma Decimal instância (O número máximo de dígitos, O número de casas decimais)
    num_decimal = models.DecimalField(max_digits=4, decimal_places=2)
    # Um campo para armazenar dados binários brutos (tamanho máximo)
    binario = models.BinaryField(max_length=10)
    # Um campo verdadeiro / falso (valor padrão verdadeiro)
    booleano = models.BooleanField(default=True)
    # Um campo de string, para strings de pequeno a grande porte (tamanho máximo)
    frase = models.CharField(max_length=20)
    # Para grandes quantidades de texto
    texto = models.TextField()
    # Um CharFieldque verifica se o valor é um endereço de e-mail válido usando EmailValidator
    email = models.EmailField(max_length=200)
    # A CharField para um URL, validado por URLValidator
    link = models.URLField()
    # Um slug é um rótulo curto para algo, contendo apenas letras, números, sublinhados ou hifens. Eles geralmente são usados ​​em URLs
    slug = models.SlugField()
    # Uma data, representada em Python por uma datetime.date instância (data agora quando atualiza ou data agora pela primeira vez ou valor padrão)
    data = models.DateField(auto_now=False)
    # Uma vez, representada em Python por uma datetime.timeinstância. Aceita as mesmas opções de preenchimento automático de DateField.
    hora = models.TimeField()
    # Uma data e hora, representadas em Python por uma datetime.datet imeinstância (mesmos que DateField)
    datahora = models.DateTimeField()
    # Um campo para armazenar períodos de tempo - modelado em Python por timedelta
    duracao = models.DurationField()
    # Um campo de upload de arquivo (nome-do-diretorio/novo-nome-do-arquivo)
    arquivo = models.FileField(upload_to=None)
    # A CharField cujas escolhas são limitadas aos nomes de arquivos em um determinado diretório no sistema de arquivos (nome do diretorio)
    caminho_de_arquivo = models.FilePathField(path=None)
    # Herda todos os atributos e métodos de FileField, mas também valida se o objeto carregado é uma imagem válida. requer pip install Pillow e
    imagem = models.ImageField(upload_to=None)