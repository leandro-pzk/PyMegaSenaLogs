from django.db import models

# Create your models here.
class PalpiteArquivoLogs(models.Model):
    
    id_parq = models.CharField(max_length=100)
    palp_file = models.CharField(max_length=500, blank=True, null=True)
    palp_file_nome = models.CharField(max_length=100, blank=True, null=True)
    parq_dt_criacao = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=100)
    user_ip = models.CharField(max_length=100)

    def __str__(self):
        return str(self.palp_file_nome)

class PalpiteLogs(models.Model):

    id_palp = models.CharField(max_length=100)
    palp_dt_criacao = models.CharField(max_length=100, blank=True, null=True)
    palp_dezenas = models.CharField(max_length=100)
    palp_file = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=100)
    user_ip = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id_palp)