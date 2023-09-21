# from django.contrib.auth import login
from audioop import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.core.paginator import Paginator
from django.http import Http404, JsonResponse

# from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms.dados_candidato_forms import DadosCandidatoForm
from formulario.models.dados_candidato_models import DadosCandidato
from formulario.models.paginations_models import Pagination
from utils.cidades_estado import obter_cidades_do_estado


@login_required(login_url="/login")
def dados_candidato(request):
    if request.method == "GET":
        dados = DadosCandidato.objects.filter(user=request.user).first()
        pagination = Pagination.objects.filter(user=request.user).first()

        for (
            field_name
        ) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_2 = "active"
        pagination.save()

        if not dados:
            form = DadosCandidatoForm()
        else:
            form = DadosCandidatoForm(instance=dados)

        return render(
            request,
            "dados_candidato.html",
            {
                "form": form,
                "pagination": pagination,
            },
        )


@login_required(login_url="/login")
def dados_candidato_enviado(request):
    if request.method == "POST":
        user = request.user
        dados, created = DadosCandidato.objects.get_or_create(user=user)
        form = DadosCandidatoForm(data=request.POST, instance=dados)
        pagination = Pagination.objects.filter(user=request.user).first()

        if form.is_valid():
            form.save()
            pagination.page_2 = "used"
            pagination.page_3 = "used"
            pagination.save()
            return redirect("formulario:formulario_email_redes_sociais")

        else:
            return render(
                request,
                "dados_candidato.html",
                {
                    "form": form,
                },
            )
    else:
        raise Http404()


def get_cidades(request):
    estado = request.GET.get("estado")
    cidades = obter_cidades_do_estado(estado)  # Implemente essa função
    return JsonResponse({"cidades": cidades})
