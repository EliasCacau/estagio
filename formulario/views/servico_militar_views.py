from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import (PunicaoServicoMilitarForm, ServicoMilitar1Form,
                              ServicoMilitar2Form)
from formulario.models import (Candidato, Dados, Pagination,
                               PunicaoServicoMilitar, Sindicato)


@login_required(login_url="/login")
def servico_militar(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_13 = "active"
        pagination.save()
        
        dados_servico_militar = Dados.objects.filter(id=candidato_id, user=request.user).first()
        form_servico_militar_1 = ServicoMilitar1Form(instance=dados_servico_militar)
        form_servico_militar_2 = ServicoMilitar2Form(instance=dados_servico_militar)

        punicao = Sindicato.objects.filter(dados_id=candidato_id).first()
        if punicao:
            form_punicao_factory = inlineformset_factory(
            Dados, PunicaoServicoMilitar, form=PunicaoServicoMilitarForm, extra=1, can_delete=True
            )
            form_punicao = form_punicao_factory(instance=objeto)
        else:
            form_punicao_factory = inlineformset_factory(
                Dados, PunicaoServicoMilitar, form=PunicaoServicoMilitarForm, extra=1, can_delete=True
            )
            form_punicao = form_punicao_factory(instance=objeto)
        context = {
            "form_servico_militar_1": form_servico_militar_1,
            "form_servico_militar_2": form_servico_militar_2,
            "form_punicao": form_punicao,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto
        }
        return render(request, "servico_militar.html", context)
    

    
@login_required(login_url="/login")
def servico_militar_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        form_servico_militar_1 = ServicoMilitar1Form(request.POST, instance=objeto)
        form_servico_militar_2 = ServicoMilitar2Form(request.POST, instance=objeto)

        form_punicao_factory = inlineformset_factory(
            Dados, PunicaoServicoMilitar, form=PunicaoServicoMilitarForm
        )
        form_punicao = form_punicao_factory(request.POST, instance=objeto)

        if form_punicao.is_valid() and form_servico_militar_1.is_valid() and form_servico_militar_2.is_valid():
            form_servico_militar_1.save()
            form_servico_militar_2.save()
            form_punicao.instance = objeto
            form_punicao.save()
            pagination.page_13 = "used"
            pagination.page_14 = "used"
            pagination.save()
            return redirect("formulario:formulario_servico_militar", objeto.id)
        else:            
            pagination.page_13 = "active"
            pagination.save()
            return render(request, "servico_militar.html", locals())
