from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import response, status
from rest_framework.decorators import action
from .models import *
from .serializers import *

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['nome', 'email', 'cpf']
    filterset_fields = ['ativo']

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo']
    filterset_fields = ['status', 'tipo','criada_por']
    ordering_fields = ['data_inicio']


class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['nome','nome_urna', 'partido_ou_chapa']
    filterset_fields = ['eleicao']

class AptidaoEleitorViewSet(viewsets.ModelViewSet):
    queryset = AptidaoELeitor.objects.all()
    serializer_class = AptidaoEleitorSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['eleicao', 'eleitor']

class RegistroVotacaoViewSet(viewsets.ModelViewSet):
    queryset = RegistroVotacao.objects.all()
    serializer_class = RegistroVotacaoSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['eleicao']
    ordering_fields = ['data_hora']


class VotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['eleicao']
