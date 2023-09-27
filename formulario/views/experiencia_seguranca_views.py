from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import (EmpregoForm, ExperienciaSegurancaForm,
                              PassagemForm)
from formulario.models import Candidato, Dados, Emprego, Pagination, Passagem


@login_required(login_url="/login")
def experiencia_seguranca(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_12 = "active"
        pagination.save()

        dados_experiencia = Dados.objects.filter(id=candidato_id, user=request.user).first()

        form_experiencia = ExperienciaSegurancaForm(instance=dados_experiencia)     

        context = {
            "form_experiencia": form_experiencia,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "experiencia_seguranca.html", context)
    

    
@login_required(login_url="/login")
def experiencia_seguranca_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        form_experiencia = ExperienciaSegurancaForm(request.POST, instance=objeto)

        if form_experiencia.is_valid():
            form_experiencia.save()
            pagination.page_12 = "used"
            pagination.page_13 = "used"
            pagination.save()
            return redirect("formulario:formulario_servico_militar", objeto.id)
        else:            
            pagination.page_12 = "active"
            pagination.save()
            return render(request, "experiencia_seguranca.html", locals())
