from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import (CartaIntencaoForm, EmpregoForm, EnderecosForm,
                              PassagemForm, PrestacaoDividaForm,
                              ProtestosDividasForm)
from formulario.models import (Candidato, Dados, Emprego, Enderecos,
                               Pagination, Passagem, PrestacaoDivida)


@login_required(login_url="/login")
def enviar_formulario(request):
    if request.method == "GET":
        return render(request, "enviar_formulario.html")