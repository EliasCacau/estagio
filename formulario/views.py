# from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import DadosCandidato


@login_required(login_url="/login")
def formulario(request):
    if request.method == "GET":
        return render(request, "formulario.html")
    else:
        user = request.user
        dados = DadosCandidato.objects.create(
            user=user,
            nome_candidato=request.POST.get("nome_candidato"),
            data_nasc_candidato=request.POST.get("data_nasc"),
        )
        dados.save()
        return HttpResponse("Formulário enviado com sucesso")
