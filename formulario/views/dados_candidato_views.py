from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import DadosCandidatoForm, TelefoneForm
from formulario.models import (Candidato, Dados, DadosCandidato, Pagination,
                               Telefone)


def lista(request):
    if request.method == "GET":
        candidato = Candidato.objects.all()
        context = {
            "lista": candidato,
        }
        return render(request, "listar_dados_candidato.html", context)

@login_required(login_url="/login")
def dados_candidato(request, candidato_id):
    if request.method == "GET":
        objeto = Dados.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        dados = Candidato.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_2 = "active"
        pagination.save()

        dados_candidato = DadosCandidato.objects.filter(user=request.user).first()
        if not dados_candidato:
            form = DadosCandidatoForm()
        else:
            form = DadosCandidatoForm(instance=dados_candidato)

        form_telefone_factory = inlineformset_factory(
            Candidato, Telefone, form=TelefoneForm, extra=1
        )
        form_telefone = form_telefone_factory(instance=dados)
        context = {
            "form_telefone": form_telefone,
            "form": form,
            "pagination": pagination,
            "to_page": to_page,
            "objeto": objeto,
        }
        return render(request, "dados_candidato.html", context)
    

    
@login_required(login_url="/login")
def dados_candidato_eviado(request, candidato_id):
    if request.method == "POST":
        objeto = Dados.objects.filter(user=request.user).first()
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Candidato.objects.filter(id=candidato_id).first()
        dados_candidato, created = DadosCandidato.objects.get_or_create(user=request.user)

        form = DadosCandidatoForm(request.POST, instance=dados_candidato)
        form_telefone_factory = inlineformset_factory(
            Candidato, Telefone, form=TelefoneForm
        )
        form_telefone = form_telefone_factory(request.POST, instance=objeto)
        if form.is_valid() and form_telefone.is_valid():
            form.save()
            form_telefone.instance = objeto
            form_telefone.save()
            pagination.page_1 = "used"
            pagination.page_2 = "used"
            pagination.save()
            return redirect(reverse("formulario:formulario_dados_adicionais"), locals())
        else:            
            pagination.page_2 = "active"
            pagination.save()
            return render(request, "dados_candidato.html", locals())

