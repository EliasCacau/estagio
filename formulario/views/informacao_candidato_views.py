from audioop import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.core.paginator import Paginator
from django.http import Http404

# from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms.informacao_candidato_forms import InformacaoCandidatoForm
from formulario.models.informacao_candidato_models import InformacaoCandidato
from formulario.models.paginations_models import Pagination


@login_required(login_url="/login")
def informacao_candidato(request):
    if request.method == "GET":
        dados = InformacaoCandidato.objects.filter(user=request.user).first()

        if not dados:
            form = InformacaoCandidatoForm()
        else:
            form = InformacaoCandidatoForm(instance=dados)

        user_pagination = Pagination.objects.filter(user=request.user).exists()
        if user_pagination:
            pagination = Pagination.objects.filter(user=request.user).first()
        else:
            pagination = Pagination()
            pagination.user = request.user
            pagination.save()

        return render(
            request,
            "informacao_candidato.html",
            {
                "form": form,
                "pagination": pagination,
            },
        )


@login_required(login_url="/login")
def informacao_candidato_enviado(request):
    if request.method == "POST":
        user = request.user
        dados, created = InformacaoCandidato.objects.get_or_create(user=user)
        form = InformacaoCandidatoForm(data=request.POST, instance=dados)
        pagination = Pagination.objects.filter(user=request.user).first()

        if form.is_valid():
            form.save()
            pagination.page_1 = "used"
            pagination.page_2 = "used"
            pagination.save()
            return redirect("formulario:formulario")
        else:
            return render(
                request,
                "informacao_candidato.html",
                context={
                    "form": form,
                },
            )
    else:
        raise Http404()
