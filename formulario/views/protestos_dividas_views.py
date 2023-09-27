from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import (EmpregoForm, EnderecosForm, PassagemForm,
                              PrestacaoDividaForm, ProtestosDividasForm)
from formulario.models import (Candidato, Dados, Emprego, Enderecos,
                               Pagination, Passagem, PrestacaoDivida)


@login_required(login_url="/login")
def protestos_dividas(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_17 = "active"
        pagination.save()
    
        form_dividas = ProtestosDividasForm(instance=objeto) 

        prestacoes_dividas = PrestacaoDivida.objects.filter(dados_id=candidato_id).first()
        if prestacoes_dividas:
            form_prestacoes_dividas_factory = inlineformset_factory(Dados, PrestacaoDivida, form=PrestacaoDividaForm, extra=1, can_delete=True)
            form_prestacoes_dividas = form_prestacoes_dividas_factory(instance=objeto)
        else:
            form_prestacoes_dividas_factory = inlineformset_factory(Dados, PrestacaoDivida, form=PrestacaoDividaForm, extra=1, can_delete=True)
            form_prestacoes_dividas = form_prestacoes_dividas_factory(instance=objeto)
        

        context = {
            "form_prestacoes_dividas": form_prestacoes_dividas,
            "form_dividas": form_dividas,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "protestos_dividas.html", context)
    

    
@login_required(login_url="/login")
def protestos_dividas_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        form_dividas = ProtestosDividasForm(request.POST, instance=objeto)

        form_prestacoes_dividas_factory = inlineformset_factory(
            Dados, PrestacaoDivida, form=PrestacaoDividaForm
        )
        form_prestacoes_dividas = form_prestacoes_dividas_factory(request.POST, instance=objeto)

        if form_dividas.is_valid() and form_prestacoes_dividas.is_valid():
            form_dividas.save()
            form_prestacoes_dividas.instance = objeto
            form_prestacoes_dividas.save()
            pagination.page_17 = "used"
            pagination.page_18 = "used"
            pagination.save()
            return redirect("formulario:formulario_patrimonio_veiculo", objeto.id)
        else:            
            pagination.page_18 = "active"
            pagination.save()
            return render(request, "protestos_dividas.html", locals())
