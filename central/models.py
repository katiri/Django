import uuid
from django.db import models
from django.urls import reverse

# documentação para campos https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
# documentação para opções Meta dos modelos https://docs.djangoproject.com/en/3.0/ref/models/options/

class Base(models.Model):
    criados = models.DateField('Criação')
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Exemplo(Base):
    # Gera um id para cada linha
    # auto_campo = models.AutoField()
    # Id maior
    # grande_auto_campo = models.BigAutoField()
    # Como um AutoField, mas só permite valores sob um certo limite (dependente do banco de dados).
    # pequeno_auto_campo = models.SmallAutoField()

    # Um campo para armazenar identificadores exclusivos universalmente. Usa a UUIDclasse Python. requer import uuid
    chave_unica = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        # editable=False,
        null=False,
        blank=False,
        unique=True,
        # Defina como o nome de a DateFieldou DateTimeFieldpara exigir que este campo seja exclusivo para o valor do campo de data.
        # Por exemplo, se você tem um campo titleque tem unique_for_date="pub_date", então o Django não permitiria a entrada de dois
        # registros com o mesmo titlee pub_date.
        # unique_for_date='criados',
        # unique_for_month='criados',
        # unique_for_year='criados',
        verbose_name='Código único do exemplo',
        help_text='Está é a chave única',
        error_messages={
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
            'invalid': 'Valor inválido.',
            # 'invalid_choice': 'Escolha inválida.',
            'unique': 'Este valor já exite no banco de dados.',
            # 'unique_for_date': 'Esta data já exite no banco de dados.'
        }
    )

    # Campo de número
    inteiro = models.IntegerField(
        verbose_name='Valor do tipo inteiro',
        help_text='Digite um valor do tipo inteiro (-2147483648 a 2147483647)',
        error_messages={
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
            'invalid': 'Valor inválido.',
        }
    )
    # Campo de número grande
    grande_inteiro = models.BigIntegerField(
        verbose_name='Valor grande do tipo inteiro',
        help_text='Digite um valor grande do tipo inteiro (-9223372036854775808 a 9223372036854775807)',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
        }
    )
    # Como um IntegerField, mas só permite valores em um determinado ponto (dependente do banco de dados)
    pequeno_inteiro = models.SmallIntegerField(
        verbose_name='Valor pequeno do tipo inteiro',
        help_text='Digite um valor pequeno do tipo inteiro (-32768 a 32767)',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
        }
    )
    # Como um IntegerField, mas deve ser positivo ou zero ( 0)
    inteiro_positivo = models.PositiveIntegerField(
        verbose_name='Valor do tipo inteiro positivo',
        help_text='Digite um valor do tipo inteiro positivo (0 a 2147483647)',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
        }
    )
    # Como um BigIntegerField, mas deve ser positivo ou zero ( 0)
    grande_inteiro_positivo = models.PositiveBigIntegerField(
        verbose_name='Valor grande do tipo inteiro positivo',
        help_text='Digite um valor grade do tipo inteiro positivo (0 a 9223372036854775807)',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
        }
    )
    # Como um SmallIntegerField, mas deve ser positivo ou zero ( 0)
    pequeno_inteiro_positivo = models.PositiveSmallIntegerField(
        verbose_name='Valor pequeno do tipo inteiro positivo',
        help_text='Digite um valor pequeno do tipo inteiro positivo (0 a 32767)',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
        }
    )
    # Um número decimal de precisão fixa, representado em Python por uma Decimal instância (O número máximo de dígitos, O número de casas decimais)
    num_decimal = models.DecimalField(
        verbose_name='Valor do tipo decimal',
        help_text='Digite um valor do tipo decimal (no máximo 2 casas decimais e 4 casas)',
        max_digits=4,
        decimal_places=2,
        error_messages={
            'invalid': 'Valor inválido.',
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
        }
    )
    # Um número de ponto flutuante representado em Python por uma float instância.
    num_float = models.FloatField(
        verbose_name='Valor do tipo float',
        help_text='Digite um valor do tipo float (no máximo duas casas decimais)',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
        }
    )
    # Um campo para armazenar dados binários brutos (tamanho máximo)
    # binario = models.BinaryField(max_length=10)
    # Um campo verdadeiro / falso (valor padrão verdadeiro)
    booleano = models.BooleanField(
        default=True,
        verbose_name='Campo checkbox, do tipo booleano',
        help_text='Este campo é verdadeiro ou falso',
    )
    # Um campo de string, para strings de pequeno a grande porte (tamanho máximo)
    frase = models.CharField(
        verbose_name='Campo de texto simples',
        help_text='Digite uma frase de até 42 caracteres',
        max_length=42,
        error_messages={
            'invalid': 'Valor inválido.',
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
        }
    )
    # Para grandes quantidades de texto
    texto = models.TextField(
        verbose_name='Campo de texto grande',
        help_text='Digite uma frase de até 500 caracteres',
        max_length=500,
        error_messages={
            'invalid': 'Valor inválido.',
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
        }
    )
    # Um CharFieldque verifica se o valor é um endereço de e-mail válido usando EmailValidator
    email = models.EmailField(
        verbose_name='Campo de email',
        help_text='Digite uma email válido de até 200 caracteres',
        max_length=200,
        error_messages={
            'invalid': 'E-mail inválido.',
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
        }
    )
    # A CharField para um URL, validado por URLValidator
    link = models.URLField(
        verbose_name='Campo de link',
        help_text='Digite um link válido de até 200 caracteres',
        max_length=200,
        error_messages={
            'invalid': 'Link inválido.',
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
        }
    )
    # Um slug é um rótulo curto para algo, contendo apenas letras, números, sublinhados ou hifens. Eles geralmente são usados ​​em URLs
    slug = models.SlugField(
        verbose_name='Campo de slug',
        help_text='Esse campo é preenchido automaticamente com a data e com a chave unica',
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'invalid': 'Valor inválido.',
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
            'unique': 'Este valor já exite no banco de dados.',
        }
    )
    # Campo select
    escolhas = [
        ('', ''),
        ('valor1', 'texto1'),
        ('valor2', 'texto2'),
        ('valor3', 'texto3'),
    ]
    selecionar = models.CharField(
        verbose_name='Campo de seleção de opções',
        help_text='Selecione uma opção',
        max_length=200,
        choices=escolhas,
        default='',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
            'invalid_choice': 'Escolha inválida',
        }
    )
    # Uma data, representada em Python por uma datetime.date instância (data agora quando atualiza ou data agora pela primeira vez ou valor padrão)
    data = models.DateField(
        verbose_name='Campo de data',
        help_text='selecione uma data no formato dd/mm/yyyy',
        auto_now=False,
        error_messages={
            'invalid': 'Valor inválido.',
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
        }
    )
    # Uma vez, representada em Python por uma datetime.timeinstância. Aceita as mesmas opções de preenchimento automático de DateField.
    hora = models.TimeField(
        verbose_name='Campo de hora',
        help_text='selecione uma hora no formato h:m:s',
        error_messages={
            'invalid': 'Valor inválido.',
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
        }
    )
    # Uma data e hora, representadas em Python por uma datetime.datet imeinstância (mesmos que DateField)
    datahora = models.DateTimeField(
        verbose_name='Campo de data e hora',
        help_text='selecione uma data-hora no formato dd/mm/yyyy h:m:s',
        error_messages={
            'invalid': 'Valor inválido.',
            'null': 'O campo não pode ser nulo.',
            'blank': 'O campo não pode ser vazio.',
        }
    )
    # Um campo para armazenar períodos de tempo - modelado em Python por timedelta
    duracao = models.DurationField(
        verbose_name='Campo de duração',
        help_text='selecione uma duração em segundos',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
        }
    )
    # Um campo de upload de arquivo (nome-do-diretorio/novo-nome-do-arquivo)
    arquivo = models.FileField(
        verbose_name='Campo de upload de arquivo',
        help_text='faça um upload de um arquivo com qualquer extenção',
        upload_to='arquivos/',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
        }
    )
    # Herda todos os atributos e métodos de FileField, mas também valida se o objeto carregado é uma imagem válida. requer pip install Pillow e
    imagem = models.ImageField(
        verbose_name='Campo de upload de imagem',
        help_text='faça um upload de uma imagem',
        upload_to='imagens/',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Valor inválido.',
        }
    )
    # A CharField cujas escolhas são limitadas aos nomes de arquivos em um determinado diretório no sistema de arquivos (nome do diretorio)
    # caminho_de_arquivo = models.FilePathField(
    #     verbose_name='Selecione o caminho de um arquivo',
    #     help_text='Selecione uma opção',
    #     path=None,
    #     error_messages={
    #         'invalid': 'Valor inválido.',
    #         'null': 'O campo não pode ser nulo.',
    #         'blank': 'O campo não pode ser vazio.',
    #     }
    # )

    class Meta:
        verbose_name = 'Exemplo'
        verbose_name_plural = 'Exemplos'
        ordering = ['chave_unica']

    # url de exibição no site
    def get_absolute_url(self):
        return reverse('LendoBancoItem', args=[str(self.chave_unica)])

    # o que aparece na lista de consulta
    def __str__(self):
        return 'Exemplo [' + str(self.chave_unica) + ']'

# https://docs.djangoproject.com/en/3.0/ref/models/fields/#foreignkey

class CamposRelacionado(Base):
    # Um relacionamento muitos para um
    chave_estrangeira = models.ForeignKey(Exemplo, on_delete=models.CASCADE, related_name='CamposRelacionado1', related_query_name='CamposRelacionado11')
    # Para criar um relacionamento muitos para um consigo mesmo
    chave_estrangeira_self = models.ForeignKey('self', on_delete=models.CASCADE, related_name='CamposRelacionado2', related_query_name='CamposRelacionado2', blank=True, null=True)
    # Um relacionamento de muitos para muitos
    muitos_para_muitos = models.ManyToManyField(Exemplo)
    # Um relacionamento de muitos para muitos consigo mesmo
    muitos_para_muitos_self = models.ManyToManyField('self', blank=True)
    # Um relacionamento um para um
    um_para_um =models.OneToOneField(to=Exemplo, on_delete=models.CASCADE, related_name='CamposRelacionado3', related_query_name='CamposRelacionado3')

    class Meta:
        verbose_name = 'Modelo de relacionamento'
        verbose_name_plural = 'Modelo de relacionamento'

    def __str__(self):
        return 'Chave estrangeira: ' + str(self.chave_estrangeira)