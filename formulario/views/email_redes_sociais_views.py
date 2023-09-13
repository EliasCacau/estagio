from audioop import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.core.paginator import Paginator
from django.http import Http404

# from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms.email_redes_sociais_forms import EmailRedesSociaisForm
from formulario.models.email_redes_sociais_models import EmailRedesSociais
from formulario.models.paginations_models import Pagination


@login_required(login_url="/login")
def formulario_email_redes_sociais(request):
    if request.method == "GET":
        dados = EmailRedesSociais.objects.filter(user=request.user).first()
        pagination = Pagination.objects.filter(user=request.user).first()

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
            pagination.page_3 = "used"
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
