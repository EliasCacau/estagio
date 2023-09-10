from django.contrib.auth.models import User
from django.db import models


class DadosBancarios(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    banco = models.CharField(max_length=100, null=False)
    num_conta = models.CharField(max_length=100, null=False)
    num_agencia = models.CharField(max_length=100, null=False)
    endereco_banco = models.CharField(max_length=100, null=False)

    banco_2 = models.CharField(max_length=100, null=True, blank=True)
    num_conta_2 = models.CharField(max_length=100, null=True, blank=True)
    num_agencia_2 = models.CharField(max_length=100, null=True, blank=True)
    endereco_banco_2 = models.CharField(max_length=100, null=True, blank=True)

    banco_3 = models.CharField(max_length=100, null=True, blank=True)
    num_conta_3 = models.CharField(max_length=100, null=True, blank=True)
    num_agencia_3 = models.CharField(max_length=100, null=True, blank=True)
    endereco_banco_3 = models.CharField(max_length=100, null=True, blank=True)
