from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import EmpregoForm, EnderecosForm, PassagemForm
from formulario.models import (Candidato, Dados, Emprego, Enderecos,
                               Pagination, Passagem)


@login_required(login_url="/login")
def enderecos(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_14 = "active"
        pagination.save()
    
        enderecos = Enderecos.objects.filter(dados_id=candidato_id).first()
        if enderecos:
            form_enderecos_factory = inlineformset_factory(Dados, Enderecos, form=EnderecosForm, extra=1, can_delete=True)
            form_enderecos = form_enderecos_factory(instance=objeto)
        else:
            form_enderecos_factory = inlineformset_factory(Dados, Enderecos, form=EnderecosForm, extra=1, can_delete=True)
            form_enderecos = form_enderecos_factory(instance=objeto)
        

        context = {
            "form_enderecos": form_enderecos,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "enderecos.html", context)
    

    
@login_required(login_url="/login")
def enderecos_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        # form_inquerito_1 = InqueritoForm1(request.POST, instance=objeto)

        form_enderecos_factory = inlineformset_factory(
            Dados, Enderecos, form=EnderecosForm
        )
        form_enderecos = form_enderecos_factory(request.POST, instance=objeto)

        if form_enderecos.is_valid():
            form_enderecos.instance = objeto
            form_enderecos.save()
            pagination.page_14 = "used"
            pagination.page_15 = "used"
            pagination.save()
            return redirect("formulario:formulario_ensino", objeto.id)
        else:            
            pagination.page_14 = "active"
            pagination.save()
            return render(request, "enderecos.html", locals())
