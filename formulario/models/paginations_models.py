from django.contrib.auth.models import User
from django.db import models


class Pagination(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    page_1 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_2 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_3 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_4 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_5 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_6 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
    page_7 = models.CharField(max_length=100, null=True, blank=True, default="disabled")
