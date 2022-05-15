import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.forms import PalpiteArquivoLogsForm
from api.models import PalpiteArquivoLogs, PalpiteLogs
from api.serializers import PalpiteArquivoSerializer
from django.core import serializers
from django.http import HttpResponse

@api_view(['POST'])
def logs_palpite_arquivo(request):
    """
    Logs model palpite_arquivos 
    """
    data = json.loads(request.data)

    try:
        form = PalpiteArquivoLogs(
            palp_file = data[0]['palp_file'], palp_file_nome = data[0]['palp_file_nome'], 
            parq_dt_criacao = data[0]['parq_dt_criacao'], id_parq = data[0]['id_parq'],
            user_name = data[0]['usuario'], user_ip = data[0]['ip'])

        form.save()

        return HttpResponse(status=200)

    except:
        return HttpResponse(status=500)    
    

@api_view(['POST'])
def logs_palpite(request):
    """
    Logs model palpite 
    """
    data = json.loads(request.data)

    try:
        form = PalpiteLogs(
            palp_file = str(data[0]['palp_file_id']), palp_dezenas = data[0]['palp_dezenas'], 
            palp_dt_criacao = data[0]['palp_dt_criacao'], id_palp = str(data[0]['id_palp']),
            user_name = data[0]['usuario'], user_ip = data[0]['ip'])

        form.save()

        return HttpResponse(status=200)

    except:
        return HttpResponse(status=500)    
    