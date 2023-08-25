# from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# from django.core.paginator import Paginator
from django.http import Http404

# from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms.dados_candidato_forms import DadosCandidatoForm, RegisterForm2

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
    form = DadosCandidatoForm(request.POST, instance=dados)
    if form.is_valid():
        dados = DadosCandidato.objects.create(
            user=user,
            nome_candidato=request.POST.get("nome_candidato"),
            data_nasc_candidato=request.POST.get("data_nasc_candidato"),
            estado_civil=request.POST.get("estado_civil"),
            apelido_candidato=request.POST.get("apelido_candidato"),
            nacionalidade=request.POST.get("nacionalidade"),
            natural=request.POST.get("natural"),
            uf_natural=request.POST.get("uf_natural"),
            nome_pai=request.POST.get("nome_pai"),
            nome_mae=request.POST.get("nome_mae"),
            idiomas=request.POST.get("idiomas"),
            num_identidade=request.POST.get("num_identidade"),
            orgao_emissor=request.POST.get("orgao_emissor"),
            num_titulo_eleitor=request.POST.get("num_titulo_eleitor"),
            zona_titulo=request.POST.get("zona_titulo"),
            num_carteira_profissional=request.POST.get("num_carteira_profissional"),
            serie_carteira_prof=request.POST.get("serie_carteira_prof"),
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
