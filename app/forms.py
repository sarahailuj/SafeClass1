from django import forms
from .models import Ocorrencia

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = [
            'anonima',
            'email_denunciante',
            'pessoa_denunciante',
            'nome_agressor',
            'ocupacao_agressor',
            'curso_agressor',
            'turma_agressor',
            'nome_vitima',
            'ocupacao_vitima',
            'curso_vitima',
            'turma_vitima',
            'tipo_ocorrencia',
            'descricao',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
