from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"

class Ocupacao(models.Model):
    TIPOS_OCUPACAO = [
        ('ALUNO', 'Aluno'),
        ('PROFESSOR', 'Professor'),
        ('FUNCIONARIO', 'Funcionário'),
        ('COORDENADOR', 'Coordenador'),
        ('DIRETOR', 'Diretor'),
    ]

    nome = models.CharField(max_length=20, choices=TIPOS_OCUPACAO, unique=True)

    def __str__(self):
        return self.get_nome_display()

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    numero_identificacao = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    nome_pai = models.CharField(max_length=100, blank=True, null=True)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


class Aluno(Pessoa):
    pass

class Servidor(Pessoa):
    siape = models.CharField(max_length=20)
    cargo = models.CharField(max_length=100)

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=150)
    site = models.URLField(blank=True)
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.curso.nome}"

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

class Ocorrencia(models.Model):
    TIPOS_OCORRENCIA = [
        ('agressao_fisica', 'Agressão física'),
        ('agressao_verbal', 'Agressão verbal'),
        ('bullying', 'Bullying'),
        ('cyberbullying', 'Cyberbullying'),
        ('psicologica', 'Violência psicológica'),
        ('ameaca', 'Ameaça'),
        ('discriminacao', 'Discriminação'),
        ('assedio_moral', 'Assédio moral'),
        ('assedio_sexual', 'Assédio sexual'),
        ('furto_roubo', 'Furto / roubo'),
        ('dano_patrimonio', 'Dano ao patrimônio'),
        ('porte_arma', 'Porte de arma'),
        ('uso_drogas', 'Uso de substância ilícita'),
        ('venda_drogas', 'Venda de substância ilícita'),
        ('violencia_domestica', 'Violência doméstica'),
        ('autolesao', 'Autolesão / tentativa de suicídio'),
        ('outros', 'Outros'),
    ]

    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)

    anonima = models.BooleanField(default=False)
    pessoa_denunciante = models.ForeignKey(
        Pessoa, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='denuncias'
    )
    email_denunciante = models.EmailField(blank=True, null=True)

    nome_agressor = models.CharField(max_length=100)
    ocupacao_agressor = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, related_name='oc_agressor')
    curso_agressor = models.CharField(max_length=100, blank=True, null=True)
    turma_agressor = models.CharField(max_length=50, blank=True, null=True)

    nome_vitima = models.CharField(max_length=100)
    ocupacao_vitima = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, related_name='oc_vitima')
    curso_vitima = models.CharField(max_length=100, blank=True, null=True)
    turma_vitima = models.CharField(max_length=50, blank=True, null=True)

    tipo_ocorrencia = models.CharField(max_length=30, choices=TIPOS_OCORRENCIA)

    def clean(self):
        from django.core.exceptions import ValidationError
        if not self.anonima and (not self.pessoa_denunciante or not self.email_denunciante):
            raise ValidationError("Denúncias não anônimas precisam de nome e e-mail do denunciante.")

class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

class HistoricoConduta(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    total_ocorrencias = models.IntegerField(default=0)
    ultimas_ocorrencias = models.TextField(blank=True)
    nivel_risco = models.CharField(
        max_length=10,
        choices=[('baixo', 'Baixo'), ('medio', 'Médio'), ('alto', 'Alto')]
    )
