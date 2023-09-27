from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import EnsinoForm, ExpulsoEnsinoForm, PassagemForm
from formulario.models import (Candidato, Dados, Emprego, Enderecos, Ensino,
                               Pagination, Passagem)


@login_required(login_url="/login")
def ensino(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_15 = "active"
        pagination.save()

        form_expulso = ExpulsoEnsinoForm(instance=objeto) 

        ensino = Ensino.objects.filter(dados_id=candidato_id).first()
        if ensino:
            form_ensino_factory = inlineformset_factory(Dados, Ensino, form=EnsinoForm, extra=1, can_delete=True)
            form_ensino = form_ensino_factory(instance=objeto)
        else:
            form_ensino_factory = inlineformset_factory(Dados, Ensino, form=EnsinoForm, extra=1, can_delete=True)
            form_ensino = form_ensino_factory(instance=objeto)
        

        context = {
            "form_expulso": form_expulso,
            "form_ensino": form_ensino,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "ensino.html", context)
    

    
@login_required(login_url="/login")
def ensino_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        form_expulso = ExpulsoEnsinoForm(request.POST, instance=objeto)

        form_ensino_factory = inlineformset_factory(
            Dados, Ensino, form=EnsinoForm
        )
        form_ensino = form_ensino_factory(request.POST, instance=objeto)

        if form_ensino.is_valid and form_expulso.is_valid():
            form_expulso.save()
            form_ensino.instance = objeto
            form_ensino.save()
            pagination.page_15 = "used"
            pagination.page_16 = "used"
            pagination.save()
            return redirect("formulario:formulario_habilitacao_motorista", objeto.id)
        else:            
            pagination.page_15 = "active"
            pagination.save()
            return render(request, "ensino.html", locals())
