# flake8: noqa

from django.contrib.auth.models import User
from django.db import models


class DadosCandidato2(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nome_candidato = models.CharField(max_length=100, null=True)
    data_nasc_candidato = models.DateField()
    # estado_civil = models.CharField(max_length=10, choices=OPCOES)
    apelido_candidato = models.CharField(max_length=60)
    nacionalidade = models.CharField(max_length=60)
    natural = models.CharField(max_length=60)
    uf_natural = models.CharField(max_length=10)


OPCOES = [
    ("Solteiro", "Solteiro"),
    ("Casado", "Casado"),
    ("Divorciado", "Divorciado"),
    ("Viúvo", "Viúvo"),
]


class DadosCandidato(models.Model):
    # opcoes = models.TextChoices("Solteiro", "Casado", "Divorciado", "Viúvo")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nome_candidato = models.CharField(max_length=100, null=True)
    data_nasc_candidato = models.DateField()
    estado_civil = models.CharField(max_length=10, choices=OPCOES, null=True)
    apelido_candidato = models.CharField(max_length=60, null=True)
    nacionalidade = models.CharField(max_length=60, null=True)
    natural = models.CharField(max_length=60, null=True)
    uf_natural = models.CharField(max_length=10, null=True)

    nome_pai = models.CharField(max_length=100, null=True)
    nome_mae = models.CharField(max_length=100, null=True)

    idiomas = models.CharField(max_length=100, null=True)

    num_identidade = models.CharField(max_length=10, null=True)
    orgao_emissor = models.CharField(max_length=10, null=True)

    num_titulo_eleitor = models.CharField(max_length=20, null=True)
    zona_titulo = models.CharField(max_length=10, null=True)

    num_carteira_profissional = models.CharField(max_length=60, null=True)
    serie_carteira_prof = models.CharField(max_length=60, null=True)
