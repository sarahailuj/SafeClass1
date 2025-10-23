from django.db import models

from django.contrib.auth.models import AbstractUser

class Cidade(models.Model):
    nome = models.CharField(max_length = 100)
    uf = models.CharField(max_length =2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"

class Ocupacao(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length = 150)
    numero_identificacao = models.CharField(max_length = 20,unique=True)
    cpf = models.CharField(max_length = 11,blank = True)
    data_nascimento = models.DateField()
    nome_pai = models.CharField(max_length = 100,blank = True,null = True)
    nome_mae = models.CharField(max_length = 100,blank = True,null = True)
    email = models.EmailField()
    telefone = models.CharField(max_length = 20)
    cidade = models.ForeignKey(Cidade,on_delete=models.SET_NULL,null = True)
    ocupacao = models.ForeignKey(Ocupacaoon_delete=models.SET_NILL,null=True)
    
    class Meta:
        abstract = True

class Aluno(Pessoa):
    pass

class Servidor (Pessoa):
    siape = models.CharField(max_length = 20)
    cargo = models.CharField(max_length = 100)

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length = 150)
    site = models.URLField(blank= True)
    telefone = models.CharField(max_length = 20)
    cidade = models.ForeignKey(Cidade,on_delete =models.SET_NULL,null = True)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length= 150)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.ImageField()
    instituicao = models.ForeignKey(InstituicaoEnsino,on_delete = models.CASCADE)

    def __str__(self):
        return self.nome
    
class Turma (models.Model):
    nome = models.CharField(max_length = 50)
    curso = models.ForeignKey(Curso,on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.nome} -{self.curso.nome}"
    
class Matricula (models.Model):
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete= models.SET_NULL,null =True)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

class TipoOcorrencia(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class Ocorrencia (models.Model):
    descricao = models.TextField()
    