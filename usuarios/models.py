from django.contrib.auth.models import User
from django.db import models


class MatriculaCpf(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuário"
    )
    num_matricula = models.CharField(max_length=50, verbose_name="Número de Matrícula")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    cadastrado = models.BooleanField(default=False, verbose_name="Cadastrado")

    class Meta:
        verbose_name = "Matrícula e CPF"
        verbose_name_plural = "Matrículas e CPFs"

    def __str__(self):
        return f"{self.user.username if self.user else 'Usuário não associado'} - {self.cpf}, {self.num_matricula}"

    @property
    def get_cpf(self):
        return self.cpf
