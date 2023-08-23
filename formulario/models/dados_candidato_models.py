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


class DadosCandidato(models.Model):
    # OPCOES = [
    #     ("Solteiro", "Solteiro"),
    #     ("Casado", "Casado"),
    #     ("Divorciado", "Divorciado"),
    #     ("Viúvo", "Viúvo"),
    # ]
    # opcoes = models.TextChoices("Solteiro", "Casado", "Divorciado", "Viúvo")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nome_candidato = models.CharField(max_length=100, null=True)
    data_nasc_candidato = models.DateField()
    # estado_civil = models.CharField(max_length=10, choices=OPCOES)
    # apelido_candidato = models.CharField(max_length=60)
    # nacionalidade = models.CharField(max_length=60)
    # natural = models.CharField(max_length=60)
    # uf_natural = models.CharField(max_length=10)

    # nome_pai = models.CharField(max_length=100)
    # nome_mae = models.CharField(max_length=100)

    # idiomas = models.CharField(max_length=100)

    # num_identidade = models.CharField(max_length=10)
    # orgao_emissor = models.CharField(max_length=10)

    # num_titulo_eleitor = models.CharField(max_length=20)
    # zona_titulo = models.CharField(max_length=10)

    # num_carteira_profissional = models.CharField(max_length=60, blank=True)
    # serie_carteira_prof = models.CharField(max_length=60)
