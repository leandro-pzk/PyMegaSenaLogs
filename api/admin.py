from django.contrib import admin

from api.models import PalpiteArquivoLogs, PalpiteLogs

# Register your models here.
admin.site.register(PalpiteArquivoLogs)
admin.site.register(PalpiteLogs)