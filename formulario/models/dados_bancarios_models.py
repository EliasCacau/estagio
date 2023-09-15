from django.contrib.auth.models import User
from django.db import models


class DadosBancarios(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="usuário"
    )
    banco = models.CharField(max_length=100, null=False, verbose_name="Banco")
    num_conta = models.CharField(max_length=100, null=False, verbose_name="N° da conta")
    num_agencia = models.CharField(
        max_length=100, null=False, verbose_name="N° da agência"
    )
    endereco_banco = models.CharField(
        max_length=100, null=False, verbose_name="Endereço do estabelecimento"
    )

    banco_2 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Banco 2"
    )
    num_conta_2 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="N° da conta 2"
    )
    num_agencia_2 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="N° da agência 2"
    )
    endereco_banco_2 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Endereço do estabelecimento 2",
    )

    banco_3 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Banco 3"
    )
    num_conta_3 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="N° da conta 3"
    )
    num_agencia_3 = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="N° da agência 3"
    )
    endereco_banco_3 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Endereço do estabelecimento 3",
    )

    class Meta:
        verbose_name = "Dados bancarios"
        verbose_name_plural = "Dados bancarios"
