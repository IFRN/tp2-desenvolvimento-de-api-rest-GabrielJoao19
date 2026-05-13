from rest_framework import serializers
from .models import *

class EleitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Eleitor
        fields = '__all__'
    
    #falta o overwrite do metodo validade, acredito que se usa o validadete_value

class EleicaoSerializer(serializers.ModelSerializer):

    status_display = serializers.CharField(source='get_status_display')
    total_candidatos = serializers.SerializerMethodField()
    total_aptos = serializers.SerializerMethodField()
    class Meta:
        model = Eleicao
        fields='__all__'

    def get_total_candidatos(self,obj):
        return obj.candidatos()
    
    def get_total_aptos(self, obj):
        return obj.count.aptos
    
class CandidatoSerializer(serializers.ModelSerializer):

    eleicao_titulo = serializers.CharField(source='eleicao.titulo', read_only=True)

    class Meta:
        model = Candidato
        fields = '__all__'

    def validate(self, attrs):
        
        if Candidato.numero == 0:
            raise serializers.ValidationError({'erro': 'zero é reservado para voto em branco na exibição de relatórios.'})
        return attrs

class AptidaoEleitorSerializer(serializers.ModelSerializer):
    eleitor_nome = serializers.CharField(source='eleitor.nome', read_only=True)
    eleicao_titulo = serializers.CharField(source='eleicao.titulo', read_only=True)
    
    class Meta:
        model = AptidaoELeitor
        fields = '__all__'

class RegistroVotacaoSerializer(serializers.ModelSerializer):

    eleitor_nome = serializers.CharField(source='eleitor.nome', read_only=True)
    eleicao_titulo = serializers.CharField(source='eleicao.titulo', read_only=True)

    class Meta:
        model= RegistroVotacao
        fields = '__all__'

class VotoSerializer(serializers.ModelSerializer):

    candidato_nome_urna = serializers.CharField(source='candidato.nome_urna', read_only=True, allow_null=True)
    branco_display = serializers.SerializerMethodField()

    class Meta:
        model=Voto
        fields = ['candidato_nome_urna','branco_display','eleicao', 'candidato', 'em_branco', 'data_hora']
        write_only_fields = ['comprovante_hash']

    def get_branco_display(self,obj):
        if obj.em_branco:
          return 'BRANCO'
        return None 

 

    


