from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import (DadosPatrimoniaisForm, PatrimonioVeiculoForm,
                              VeiculoForm)
from formulario.models import (Candidato, Dados, DadosPatrimoniais, Pagination,
                               Veiculos)


@login_required(login_url="/login")
def patrimonio_veiculo(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_18 = "active"
        pagination.save()
    
        form_patrimonio = PatrimonioVeiculoForm(instance=objeto) 

        dados_patrimonio = DadosPatrimoniais.objects.filter(dados_id=candidato_id).first()
        if dados_patrimonio:
            form_dados_patrimonio_factory = inlineformset_factory(Dados, DadosPatrimoniais, form=DadosPatrimoniaisForm, extra=1, can_delete=True)
            form_dados_patrimonio = form_dados_patrimonio_factory(instance=objeto)
        else:
            form_dados_patrimonio_factory = inlineformset_factory(Dados, DadosPatrimoniais, form=DadosPatrimoniaisForm, extra=1, can_delete=True)
            form_dados_patrimonio = form_dados_patrimonio_factory(instance=objeto)

        veiculos = DadosPatrimoniais.objects.filter(dados_id=candidato_id).first()
        if veiculos:
            form_veiculos_factory = inlineformset_factory(Dados, Veiculos, form=VeiculoForm, extra=1, can_delete=True)
            form_veiculos = form_veiculos_factory(instance=objeto)
        else:
            form_veiculos_factory = inlineformset_factory(Dados, Veiculos, form=VeiculoForm, extra=1, can_delete=True)
            form_veiculos = form_veiculos_factory(instance=objeto)
        

        context = {
            "form_veiculos" : form_veiculos,
            "form_dados_patrimonio": form_dados_patrimonio,
            "form_patrimonio": form_patrimonio,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "patrimonio_veiculo.html", context)
    

    
@login_required(login_url="/login")
def patrimonio_veiculo_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        form_patrimonio = PatrimonioVeiculoForm(request.POST, instance=objeto)

        form_veiculos_factory = inlineformset_factory(
            Dados, Veiculos, form=VeiculoForm
        )
        form_veiculos = form_veiculos_factory(request.POST, instance=objeto)

        form_dados_patrimoniais_factory = inlineformset_factory(
            Dados, DadosPatrimoniais, form=DadosPatrimoniaisForm
        )
        form_dados_patrimoniais = form_dados_patrimoniais_factory(request.POST, instance=objeto)

        if form_patrimonio.is_valid() and form_dados_patrimoniais.is_valid() and form_veiculos.is_valid():
            form_veiculos.save()
            form_veiculos.instance = objeto
            form_dados_patrimoniais.save()
            form_dados_patrimoniais.instance = objeto
            form_patrimonio.save()
            pagination.page_18 = "used"
            pagination.page_19 = "used"
            pagination.save()
            return redirect("formulario:formulario_carta_intencao", objeto.id)
        else:            
            pagination.page_18 = "active"
            pagination.save()
            return render(request, "patrimonio_veiculo.html", locals())
