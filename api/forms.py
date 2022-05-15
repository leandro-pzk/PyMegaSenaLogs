from django import forms

from api.models import PalpiteArquivoLogs, PalpiteLogs



class PalpiteArquivoLogsForm(forms.ModelForm):
    class Meta:
        model = PalpiteArquivoLogs
        exclude = ()
        
class PalpiteLogsForm(forms.ModelForm):
    class Meta:
        model = PalpiteLogs
        exclude = ()
      