from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import (EnsinoForm, ExpulsoEnsinoForm,
                              HabilitacaoMotoristaForm, PassagemForm)
from formulario.models import (Candidato, Dados, Emprego, Enderecos, Ensino,
                               Pagination, Passagem)


@login_required(login_url="/login")
def habilitacao_motorista(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_16 = "active"
        pagination.save()

        form_habilitacao = HabilitacaoMotoristaForm(instance=objeto)         

        context = {
            "form_habilitacao": form_habilitacao,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "habilitacao_motorista.html", context)
    

    
@login_required(login_url="/login")
def habilitacao_motorista_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        form_habilitacao = HabilitacaoMotoristaForm(request.POST, instance=objeto)

        if form_habilitacao.is_valid:
            form_habilitacao.save()
            pagination.page_16 = "used"
            pagination.page_17 = "used"
            pagination.save()
            return redirect("formulario:formulario_protestos_dividas", objeto.id)
        else:            
            pagination.page_16 = "active"
            pagination.save()
            return render(request, "habilitacao_motorista.html", locals())
