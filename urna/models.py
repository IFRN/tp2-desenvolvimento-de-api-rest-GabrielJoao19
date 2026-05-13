from django.db import models

class TipoEleicaoEnum(models.TextChoices):
    'ESTUDANTIL' = 'ESTUDANTIL', 'estudantil'
    'SIDICAL' = 'SINDICAL', 'sindical'
    'ASSOCIACAO' = 'ASSOCIACAO', 'associacao'
    'CONDOMINIO' = 'CONDOMINIO', 'condominio'
    'CONSELHO' = 'CONSELHO', 'conselho'
    'OUTRA' = 'OUTRA', 'outra'

class StatusEleicaoEnum(models.TextChoices):
    'RASCUNHO' = 'RASCUNHO', 'rascunho'
    'ABERTA' = 'ABERTA', 'aberta'
    'ENCERRADA' = 'ENCERRADA', 'encerrada'
    'APURADA' = 'APURADA', 'apurada'

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
    titulo = models.CharField(max_length=200)
    descricao =  models.TextField(blank=True)
    tipo =  models.CharField(choices=TipoEleicaoEnum.choices)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    status = models.CharField(choices=StatusEleicaoEnum.choices, default=)#falta finalizar
    permite_branco = models.BooleanField()
    criada_por = models.ForeignKey(Eleitor, on_delete=PROTECT,related_name='eleicoes_criadas')

class Candidato(models.Model):
    eleicao = models.ForeignKey(Eleicao, on_delete=CASCADE, related_name='candidatos')
    numero = models.PositiveIntegerField()
    nome = models.CharField(max_length=150)
    nome_urna = models.CharField(max_length=50)
    partido_ou_chapa = models.CharField(max_length=100, blank=True)
    proposta = models.TextField(blank=True)
    foto_url = models.URLField()

    #falta colocar o META

class AptidaoELeitor(models.Model):
    eleitor = models.ForeignKey(Eleitor, on_delete=PROTECT, related_name='aptidoes')
    eleicao = models.ForeignKey(ELeicao, on_delete=CASCADE, related_name='aptos')
    data_inclusao = models.DateTimeField(auto_now_add=True)

    #feito o META, so nao sei se ta certo
    class Meta:
        unique_together = [('eleicao', 'numero')]

class RegistroVotacao(models.Model):
    eleitor = models.ForeignKey(Eleitor, on_delete=PROTECT, related_name='registros_votacao')
    eleicao = models.ForeignKey(Eleicao, on_delete=PROTECT, related_name='registros_votacao')
    data_hora = models.DateTimeField(auto_now_add=True)

    #falta colocar o META


class Voto(models.Model):
    eleicao = models.ForeignKey(Eleicao, on_delete=PROTECT, related_name='votos')
    candidato = models.ForeignKey(Candidato, on_delete=PROTECT, related_name='votos',null=True, blank=True)
    em_branco = models.BooleanField(default=False)
    data_hora = models.DateTimeField(auto_now_add=True)
    comprovante_hash = models.CharField(max_length=64, unique=True)

    #falta o metodo clean



                                        
