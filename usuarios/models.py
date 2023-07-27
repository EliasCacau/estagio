from django.contrib.auth.models import User
from django.db import models


class MatriculaCpf(models.Model):
    id_matricula_cpf = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    num_matricula = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    cadastrado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username if self.user else 'Usuário não associado'} - {self.cpf}, {self.num_matricula}"

    @property
    def get_cpf(self):
        return self.cpf
