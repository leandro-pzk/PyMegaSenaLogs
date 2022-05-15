from rest_framework import serializers

from api.models import PalpiteArquivoLogs, PalpiteLogs


class PalpiteArquivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PalpiteArquivoLogs
        fields = '__all__'


class PalpiteLogsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PalpiteLogs
        fields = '__all__'