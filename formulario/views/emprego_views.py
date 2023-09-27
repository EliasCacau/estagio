from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import EmpregoForm, PassagemForm
from formulario.models import Candidato, Dados, Emprego, Pagination, Passagem


@login_required(login_url="/login")
def emprego(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_11 = "active"
        pagination.save()

        # dados_inquerito = Dados.objects.filter(id=candidato_id, user=request.user).first()

        # form_inquerito_1 = InqueritoForm1(instance=dados_inquerito)

    
        emprego = Emprego.objects.filter(dados_id=candidato_id).first()
        if emprego:
            form_emprego_factory = inlineformset_factory(Dados, Emprego, form=EmpregoForm, extra=1, can_delete=True)
            form_emprego = form_emprego_factory(instance=objeto)
        else:
            form_emprego_factory = inlineformset_factory(Dados, Emprego, form=EmpregoForm, extra=1, can_delete=True)
            form_emprego = form_emprego_factory(instance=objeto)
        

        context = {
            "form_emprego": form_emprego,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "emprego.html", context)
    

    
@login_required(login_url="/login")
def emprego_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()
        print(candidato_id)
        # form_inquerito_1 = InqueritoForm1(request.POST, instance=objeto)

        form_emprego_factory = inlineformset_factory(
            Dados, Emprego, form=EmpregoForm
        )
        form_emprego = form_emprego_factory(request.POST, instance=objeto)

        if form_emprego.is_valid():
            form_emprego.instance = objeto
            form_emprego.save()
            pagination.page_11 = "used"
            pagination.page_12 = "used"
            pagination.save()
            return redirect("formulario:formulario_experiencia_seguranca", objeto.id)
        else:            
            pagination.page_11 = "active"
            pagination.save()
            return render(request, "emprego.html", locals())
