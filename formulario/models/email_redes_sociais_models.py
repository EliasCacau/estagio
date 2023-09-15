# flake8: noqa
from django.contrib.auth.models import User
from django.db import models


class EmailRedesSociais(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuário"
    )
    email = models.CharField(max_length=100, null=False)
    email_2 = models.CharField(max_length=100, null=True, blank=True)
    email_3 = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    outros = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Email e redes sociais"
        verbose_name_plural = "Emails e redes sociais"
        # ordering = ["-data"]
