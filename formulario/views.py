# from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404

# from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms.candidato_forms import DadosCandidatoForm, RegisterForm2

from .models.dados_candidato_models import DadosCandidato


@login_required(login_url="/login")
def formulario(request):
    register_form_data = request.session.get("register_form_data", None)
    if register_form_data:
        form = DadosCandidatoForm(register_form_data)
        return render(
            request,
            "formulario.html",
            {
                "form": form,
            },
        )
    else:
        form = DadosCandidatoForm()
        return render(
            request,
            "formulario.html",
            {
                "form": form,
            },
        )


@login_required(login_url="/login")
def formulario_enviado(request):
    if not request.POST:
        raise Http404()

    user = request.user
    dados = DadosCandidato.objects.filter(user=user).first()
    POST = request.POST
    request.session["register_form_data"] = POST

    dados = DadosCandidato.objects.create(
        user=user,
        nome_candidato=request.POST.get("nome_candidato"),
        data_nasc_candidato=request.POST.get("data_nasc_candidato"),
    )
    dados.save()
    return redirect("formulario:formulario")


@login_required(login_url="/login")
def formulario_2(request):
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm2(register_form_data)
    return render(
        request,
        "formulario_2.html",
        {
            "form": form,
        },
    )


@login_required(login_url="/login")
def formulario_enviado_2(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session["register_form_data"] = POST
    return redirect("formulario:formulario_2")
