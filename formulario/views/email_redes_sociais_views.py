from audioop import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
from django.http import Http404
# from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms import EmailRedesSociaisForm
from formulario.models import Candidato, EmailRedesSociais, Pagination


@login_required(login_url="/login")
def formulario_email_redes_sociais(request):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        dados = EmailRedesSociais.objects.filter(user=request.user).first()
        pagination = Pagination.objects.filter(user=request.user).first()

        for (
            field_name
        ) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_4 = "active"
        pagination.save()

        if not dados:
            form = EmailRedesSociaisForm()
        else:
            form = EmailRedesSociaisForm(instance=dados)

        return render(
            request,
            "email_redes_sociais.html",
            {
                "form": form,
                "pagination": pagination,
                "dados": dados,
                "to_page": to_page,
            },
        )


@login_required(login_url="/login")
def formulario_email_redes_sociais_enviado(request):
    if request.method == "POST":
        user = request.user
        dados, created = EmailRedesSociais.objects.get_or_create(user=user)
        form = EmailRedesSociaisForm(data=request.POST, instance=dados)
        pagination = Pagination.objects.filter(user=request.user).first()

        if form.is_valid():
            form.save()
            pagination.page_4 = "used"
            pagination.page_5 = "used"
            pagination.save()
            return redirect("formulario:formulario_dados_bancarios")
        else:
            return render(
                request,
                "email_redes_sociais.html",
                context={
                    "form": form,
                },
            )
    else:
        raise Http404()
