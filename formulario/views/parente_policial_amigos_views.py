from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import AmigosForm, ParentePolicialForm
from formulario.models import Candidato, Dados, Pagination, ParentePolicial


@login_required(login_url="/login")
def parente_policial_amigos(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_8 = "active"
        pagination.save()
        
        dados_amigos, created = Dados.objects.get_or_create(user=request.user)
        form_amigos = AmigosForm(instance=dados_amigos)

        form_parente_policial_factory = inlineformset_factory(
            Dados, ParentePolicial, form=ParentePolicialForm, extra=1
        )
        form_parente_policial = form_parente_policial_factory(instance=objeto)
        context = {
            "form_parente_policial": form_parente_policial,
            "form_amigos": form_amigos,
            "pagination": pagination,
            "to_page": to_page,
        }
        return render(request, "parente_policial_amigos.html", context)
    

    
@login_required(login_url="/login")
def parente_policial_amigos_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        form_amigos = AmigosForm(request.POST, instance=objeto)

        form_parente_policial_factory = inlineformset_factory(
            Dados, ParentePolicial, form=ParentePolicialForm
        )
        form_parente_policial = form_parente_policial_factory(request.POST, instance=objeto)
        if form_amigos.is_valid() and form_parente_policial.is_valid():
            form_amigos.save()
            form_parente_policial.instance = objeto
            form_parente_policial.save()
            pagination.page_8 = "used"
            pagination.page_9 = "used"
            pagination.save()
            return redirect("formulario:formulario_hobbies_clube", objeto.id)
        else:            
            pagination.page_8 = "active"
            pagination.save()
            return render(request, "parente_policial_amigos.html", locals())
