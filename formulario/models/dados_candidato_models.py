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
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="usuário"
    )
    nome_candidato = models.CharField(
        max_length=100, null=True, verbose_name="nome do candidato"
    )
    data_nasc_candidato = models.DateField(null=True, verbose_name="data de nascimento")
    estado_civil = models.CharField(
        max_length=10, choices=OPCOES, null=True, verbose_name="estado civil"
    )
    apelido_candidato = models.CharField(
        max_length=60, null=True, verbose_name="apelido"
    )
    nacionalidade = models.CharField(
        max_length=60, null=True, verbose_name="nacionalidade"
    )
    uf_natural = models.CharField(
        max_length=60,
        choices=estados_brasil(),
        null=True,
        verbose_name="Estado de naturalidade",
    )
    natural = models.CharField(
        max_length=60,
        choices=cidades_brasil(),
        null=True,
        verbose_name="Cidade de naturalidade",
    )

    nome_pai = models.CharField(max_length=100, null=True, verbose_name="nome do pai")
    nome_mae = models.CharField(max_length=100, null=True, verbose_name="nome da mae")

    idiomas = models.CharField(max_length=100, null=True)

    num_identidade = models.CharField(
        max_length=10, null=True, verbose_name="N° Identidade"
    )
    orgao_emissor = models.CharField(
        max_length=10, null=True, verbose_name="Orgão Emissor"
    )

    num_titulo_eleitor = models.CharField(
        max_length=20, null=True, verbose_name="N° título de eleitor"
    )
    zona_titulo = models.CharField(
        max_length=10, null=True, verbose_name="Zona do título"
    )

    num_carteira_profissional = models.CharField(
        max_length=60, null=True, verbose_name="N° carteira profissional"
    )
    serie_carteira_prof = models.CharField(
        max_length=60, null=True, verbose_name="Série carteira profissional"
    )

    # def data_nasc_formatada(self):
    #     if self.data_nasc_candidato:
    #         return formats.date_format(self.data_nasc_candidato, "SHORT_DATE_FORMAT")
    #     return ""
