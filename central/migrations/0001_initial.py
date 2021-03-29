# Generated by Django 3.1.7 on 2021-03-29 04:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exemplos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('chave_unica', models.UUIDField(default=uuid.uuid4)),
                ('inteiro', models.IntegerField()),
                ('grande_inteiro', models.BigIntegerField()),
                ('pequeno_inteiro', models.SmallIntegerField()),
                ('inteiro_positivo', models.PositiveIntegerField()),
                ('grande_inteiro_positivo', models.PositiveBigIntegerField()),
                ('pequeno_inteiro_positivo', models.PositiveSmallIntegerField()),
                ('num_float', models.FloatField()),
                ('num_decimal', models.DecimalField(decimal_places=2, max_digits=4)),
                ('binario', models.BinaryField(max_length=10)),
                ('booleano', models.BooleanField(default=True)),
                ('frase', models.CharField(max_length=20)),
                ('texto', models.TextField()),
                ('email', models.EmailField(max_length=200)),
                ('link', models.URLField()),
                ('slug', models.SlugField()),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('datahora', models.DateTimeField()),
                ('duracao', models.DurationField()),
                ('arquivo', models.FileField(upload_to=None)),
                ('caminho_de_arquivo', models.FilePathField(path=None)),
                ('imagem', models.ImageField(upload_to=None)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
