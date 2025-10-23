from django.contrib import admin
from .models import Cidade, Ocupacao, Pessoa, Aluno, Servidor, InstituicaoEnsino, Curso, Turma, Matricula, Ocorrencia, Frequencia, HistoricoConduta

admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Aluno)
admin.site.register(Servidor)
admin.site.register(InstituicaoEnsino)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Matricula)
admin.site.register(Ocorrencia)
admin.site.register(Frequencia)
admin.site.register(HistoricoConduta)
