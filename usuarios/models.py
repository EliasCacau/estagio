from django.db import models


class MatriculaCpf(models.Model):
    id_matricula_cpf = models.AutoField(primary_key=True)
    num_matricula = models.IntegerField()
    cpf = models.IntegerField()
