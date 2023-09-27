from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import (CartaIntencaoForm, EmpregoForm, EnderecosForm,
                              PassagemForm, PrestacaoDividaForm,
                              ProtestosDividasForm)
from formulario.models import (Candidato, Dados, Emprego, Enderecos,
                               Pagination, Passagem, PrestacaoDivida)


@login_required(login_url="/login")
def carta_intencao(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_19 = "active"
        pagination.save()
    
        form_carta_intencao = CartaIntencaoForm(instance=objeto)      

        context = {
            "form_carta_intencao": form_carta_intencao,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "carta_intencao.html", context)
    

    
@login_required(login_url="/login")
def carta_intencao_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        form_carta_intencao = CartaIntencaoForm(request.POST, instance=objeto)

        if form_carta_intencao.is_valid():
            form_carta_intencao.save()
            pagination.page_19 = "used"
            pagination.page_20 = "used"
            pagination.save()
            return render(request, "enviar_formulario.html", locals())
        else:            
            pagination.page_19 = "active"
            pagination.save()
            return render(request, "carta_intencao.html", locals())
