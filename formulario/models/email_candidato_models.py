# flake8: noqa
from django.contrib.auth.models import User
from django.db import models


class EmailCandidato(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    email_candidato = models.CharField(max_length=100, null=False)
