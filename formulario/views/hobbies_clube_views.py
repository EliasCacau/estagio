from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import HobbiesClubeForm, SindicatoForm
from formulario.models import Candidato, Dados, Pagination, Sindicato


@login_required(login_url="/login")
def hobbies_clube(request, candidato_id):
    if request.method == "GET":
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_9 = "active"
        pagination.save()
        
        dados_hobbies, created = Dados.objects.get_or_create(user=request.user)
        form_hobbies = HobbiesClubeForm(instance=dados_hobbies)

        form_sindicato_factory = inlineformset_factory(
            Dados, Sindicato, form=SindicatoForm, extra=1
        )
        form_sindicato = form_sindicato_factory(instance=objeto)
        context = {
            "form_sindicato": form_sindicato,
            "form_hobbies": form_hobbies,
            "pagination": pagination,
            "to_page": to_page,
        }
        return render(request, "hobbies_clube.html", context)
    

    
@login_required(login_url="/login")
def hobbies_clube_enviado(request, candidato_id):
    if request.method == "POST":
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Dados.objects.filter(id=candidato_id).first()

        form_hobbies = HobbiesClubeForm(request.POST, instance=objeto)

        form_sindicato_factory = inlineformset_factory(
            Dados, Sindicato, form=SindicatoForm
        )
        form_sindicato = form_sindicato_factory(request.POST, instance=objeto)
        if form_sindicato.is_valid() and form_hobbies.is_valid():
            form_hobbies.save()
            form_sindicato.instance = objeto
            form_sindicato.save()
            pagination.page_9 = "used"
            pagination.page_10 = "used"
            pagination.save()
            return redirect("formulario:formulario_hobbies_clube", objeto.id)
        else:            
            pagination.page_9 = "active"
            pagination.save()
            return render(request, "hobbies_clube.html", locals())
