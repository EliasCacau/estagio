# from django.contrib.auth import login
from audioop import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
# from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms import ConjugeFamiliaForm
from formulario.models import Candidato, Dados, Pagination
from utils.cidades_estado import obter_cidades_do_estado


@login_required(login_url="/login")
def conjuge_familia(request):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        dados = Dados.objects.filter(user=request.user).first()
        pagination = Pagination.objects.filter(user=request.user).first()

        for (
            field_name
        ) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_7 = "active"
        pagination.save()

        if not dados:
            form = ConjugeFamiliaForm()
        else:
            form = ConjugeFamiliaForm(instance=dados)

        return render(
            request,
            "conjuge_familia.html",
            {
                "form": form,
                "pagination": pagination,
                "dados": dados,
                "to_page": to_page,
            },
        )


@login_required(login_url="/login")
def conjuge_familia_enviado(request):
    if request.method == "POST":
        to_page = Candidato.objects.filter(user=request.user).first()
        user = request.user
        dados, created = Dados.objects.get_or_create(user=user)
        form = ConjugeFamiliaForm(data=request.POST, instance=dados)
        pagination = Pagination.objects.filter(user=request.user).first()

        if form.is_valid():
            form.save()
            pagination.page_7 = "used"
            pagination.page_8 = "used"
            pagination.save()
            objeto = Dados.objects.filter(user=request.user).first()
            return redirect("formulario:formulario_parente_policial_amigos", objeto.id)

        else:
            return render(
                request,
                "conjuge_familia.html",
                locals()
            )
    else:
        raise Http404()

