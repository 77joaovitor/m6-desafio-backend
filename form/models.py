from django.db import models

class Transation(models.Model):
    tipo = models.IntegerField()
    data = models.CharField(max_length=10)
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=20)
    hora = models.CharField(max_length=10)
    dono_da_loja = models.CharField(max_length=50)
    nome_da_loja = models.CharField(max_length=50)
