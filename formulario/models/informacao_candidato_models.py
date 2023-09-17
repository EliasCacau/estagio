# flake8: noqa
from django.contrib.auth.models import User
from django.db import models

OPCOES_CARGO = [
    ("Delegado", "Delegado"),
    ("Investigador", "Investigador"),
    ("Escrivão", "Escrivão"),
    ("Perito", "Perito"),
    ("Criminal", "Criminal"),
    ("Papiloscopista", "Papiloscopista"),
    ("Médico Legista", "Médico Legista"),
    ("Auxiliar de Necropsia", "Auxiliar de Necropsia"),
    ("Tercerizado", "Tercerizado"),
]


def user_directory_path(instance, filename):
    # A função recebe uma instância do modelo e o nome do arquivo
    # Aqui, usamos o username do usuário para criar um subdiretório
    return f"formulario/images/{instance.user.username}/{filename}"


class InformacaoCandidato(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuário"
    )
    cargo = models.CharField(
        max_length=100,
        choices=OPCOES_CARGO,
        null=True,
        verbose_name="Cargo",
    )
    portador_necess_especial = models.CharField(
        max_length=3, choices=(("Sim", "Sim"), ("Não", "Não"))
    )
    num_cid = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="N° C.I.D",
    )
    foto = models.ImageField(
        # upload_to=f"formulario/images/{user}",
        upload_to=user_directory_path,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Informações do candidato"
        verbose_name_plural = "Informações dos candidatos"
