from django.db import models

# Create your models here.
class Eleitor(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(unique=True)
    cpf = models.CharField(max_length=14,unique=True)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
                                        
class Eleicao(models.Model):

    STATUS = [
        ('RASCUNHO', 'rascunho'),
        ('ABERTA', 'aberta'),
        ('ENCERRADA', 'encerrada'),
        ('APURADA', 'apurada')
    ]

    TIPO = [
        ('ESTUDANTIL', 'estudantil'),
        ('SINDICAL', 'sindical'),
        ('ASSOCIACAO', 'associacao'),
        ('CONDOMINIO', 'condominio'),
        ('CONSELHO', 'conselho'),
        ('OUTRA', 'outra'),
    ]

    titulo = models.CharField(max_length=200)
    descricao =  models.TextField(blank=True)
    tipo =  models.CharField(choices=TIPO)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    status = models.CharField(choices=STATUS)
    permite_branco = models.BooleanField()
    criada_por = models.ForeignKey(Eleitor, on_delete=models.PROTECT,related_name='eleicoes_criadas')

class Candidato(models.Model):
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE, related_name='candidatos')
    numero = models.PositiveIntegerField()
    nome = models.CharField(max_length=150)
    nome_urna = models.CharField(max_length=50)
    partido_ou_chapa = models.CharField(max_length=100, blank=True)
    proposta = models.TextField(blank=True)
    foto_url = models.URLField()

    #falta colocar o META

class AptidaoELeitor(models.Model):
    eleitor = models.ForeignKey(Eleitor, on_delete=models.PROTECT, related_name='aptidoes')
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE, related_name='aptos')
    data_inclusao = models.DateTimeField(auto_now_add=True)

    #falta o META


class RegistroVotacao(models.Model):
    eleitor = models.ForeignKey(Eleitor, on_delete=models.PROTECT, related_name='registros_votacao')
    eleicao = models.ForeignKey(Eleicao, on_delete=models.PROTECT, related_name='registros_votacao')
    data_hora = models.DateTimeField(auto_now_add=True)

    #falta colocar o META


class Voto(models.Model):
    eleicao = models.ForeignKey(Eleicao, on_delete=models.PROTECT, related_name='votos')
    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT, related_name='votos',null=True, blank=True)
    em_branco = models.BooleanField(default=False)
    data_hora = models.DateTimeField(auto_now_add=True)
    comprovante_hash = models.CharField(max_length=64, unique=True)

    #falta o metodo clean



                                        
