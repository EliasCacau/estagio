# flake8: noqa

from django.contrib.auth.models import User
from django.db import models
from django.utils import formats

from utils.cidades import cidades_brasil
from utils.estados import estados_brasil

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
    data_nasc_candidato = models.DateField(null=True)
    estado_civil = models.CharField(max_length=10, choices=OPCOES, null=True)
    apelido_candidato = models.CharField(max_length=60, null=True)
    nacionalidade = models.CharField(max_length=60, null=True)
    uf_natural = models.CharField(max_length=60, choices=estados_brasil(), null=True)
    natural = models.CharField(max_length=60, choices=cidades_brasil(), null=True)

    nome_pai = models.CharField(max_length=100, null=True)
    nome_mae = models.CharField(max_length=100, null=True)

    idiomas = models.CharField(max_length=100, null=True)

    num_identidade = models.CharField(max_length=10, null=True)
    orgao_emissor = models.CharField(max_length=10, null=True)

    num_titulo_eleitor = models.CharField(max_length=20, null=True)
    zona_titulo = models.CharField(max_length=10, null=True)

    num_carteira_profissional = models.CharField(max_length=60, null=True)
    serie_carteira_prof = models.CharField(max_length=60, null=True)

    # def data_nasc_formatada(self):
    #     if self.data_nasc_candidato:
    #         return formats.date_format(self.data_nasc_candidato, "SHORT_DATE_FORMAT")
    #     return ""
