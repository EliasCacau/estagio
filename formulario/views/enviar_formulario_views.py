import random

from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView
from datetime import date
from formulario.models import Dados


# Função para gerar um número de protocolo aleatório
def gerar_numero_protocolo():
    # Gere um número aleatório de 6 dígitos
    numero = random.randint(100000, 999999)
    return str(numero)

# Use a função para gerar um número de protocolo


@login_required(login_url="/login")
def enviar_formulario(request, candidato_id):
    if request.method == "GET":
        objeto = Dados.objects.filter(id=candidato_id).first()
        if not objeto.numero_protocolo:
            num_protocolo = gerar_numero_protocolo()
            objeto.data_protocolo = date.today()
            objeto.numero_protocolo = num_protocolo
            objeto.save()
        context = {'objeto': objeto}  # Crie um dicionário com as variáveis de contexto
        return render(request, "enviar_formulario.html", context)