from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ONGProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_da_ong = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email_contato = models.EmailField()
    area_atuacao = models.CharField(max_length=255)
    descricao = models.TextField()
    site = models.URLField()
    responsavel_legal = models.CharField(max_length=255)
    documentos = models.FileField(upload_to='documentos/', blank=True, null=True)  
    logotipo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.nome_da_ong

class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email_alternativo = models.EmailField()
    profissao = models.CharField(max_length=255)
    habilidades = models.TextField()
    disponibilidade = models.CharField(max_length=255)
    areas_interesse = models.CharField(max_length=255)
    experiencia_previa = models.TextField()
    motivacao = models.TextField()
    referencias = models.TextField()
    foto_perfil = models.ImageField(upload_to='fotos_perfil/')

    def __str__(self):
        return self.nome_completo
