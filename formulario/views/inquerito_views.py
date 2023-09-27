from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import (InqueritoForm1, InqueritoForm2, PassagemForm,
                              ProcessosIntimadoForm, SindicatoForm)
from formulario.models import (Candidato, Dados, Pagination, Passagem,
                               ProcessosIntimado, Sindicato)


@login_required(login_url="/login")
def inquerito(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_10 = "active"
        pagination.save()

        dados_inquerito = Dados.objects.filter(id=candidato_id, user=request.user).first()

        form_inquerito_1 = InqueritoForm1(instance=dados_inquerito)
        form_inquerito_2 = InqueritoForm2(instance=dados_inquerito)
    
        intimado = ProcessosIntimado.objects.filter(dados_id=candidato_id).first()
        if intimado:
            form_intimado_factory = inlineformset_factory(Dados, ProcessosIntimado, form=ProcessosIntimadoForm, extra=1, can_delete=True)
            form_intimado = form_intimado_factory(instance=objeto)
        else:
            form_intimado_factory = inlineformset_factory(Dados, ProcessosIntimado, form=ProcessosIntimadoForm, extra=1, can_delete=True)
            form_intimado = form_intimado_factory(instance=objeto)

        passagem = Passagem.objects.filter(dados_id=candidato_id).first()
        if passagem:
            form_passagem_factory = inlineformset_factory(Dados, Passagem, form=PassagemForm, extra=False, can_delete=True)
            form_passagem = form_passagem_factory(instance=objeto)
        else:
            form_passagem_factory = inlineformset_factory(Dados, Passagem, form=PassagemForm, extra=1, can_delete=True)
            form_passagem = form_passagem_factory(instance=objeto)
        

        context = {
            "form_intimado": form_intimado,
            "form_passagem": form_passagem,
            "form_inquerito_1": form_inquerito_1,
            "form_inquerito_2": form_inquerito_2,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "inquerito.html", context)
    

    
@login_required(login_url="/login")
def inquerito_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        form_inquerito_1 = InqueritoForm1(request.POST, instance=objeto)
        form_inquerito_2 = InqueritoForm2(request.POST, instance=objeto)

        form_intimado_factory = inlineformset_factory(
            Dados, ProcessosIntimado, form=ProcessosIntimadoForm
        )
        form_intimado = form_intimado_factory(request.POST, instance=objeto)

        form_passagem_factory = inlineformset_factory(
            Dados, Passagem, form=PassagemForm
        )
        form_passagem = form_passagem_factory(request.POST, instance=objeto)
        if form_passagem.is_valid() and form_intimado.is_valid() and form_inquerito_1.is_valid() and form_inquerito_2.is_valid():
            form_passagem.save()
            form_inquerito_1.save()
            form_inquerito_2.save()
            form_intimado.instance = objeto
            form_intimado.save()
            pagination.page_10 = "used"
            pagination.page_11 = "used"
            pagination.save()
            return redirect("formulario:formulario_emprego", objeto.id)
        else:            
            pagination.page_10 = "active"
            pagination.save()
            return render(request, "inquerito.html", locals())
