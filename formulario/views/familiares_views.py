from audioop import reverse

from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms import DadosFilhoForm, FamiliaresForm, FilhoForm
from formulario.models import Candidato, Dados, Familiares, Filho, Pagination

# Create your views here.



@login_required(login_url="/login")
def familiares(request, candidato_id):
    if request.method == "GET":
        objeto = Dados.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        dados = Candidato.objects.filter(id=candidato_id, user=request.user).first()

        pagination = Pagination.objects.filter(user=request.user).first()
        for (field_name) in pagination._meta.fields:  # Itera pelos campos do dados Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_6 = "active"
        pagination.save()

        dados_filho, created = Dados.objects.get_or_create(user=request.user)
        
        form_dados_filho = DadosFilhoForm(instance=dados_filho)

        form_filho_factory = inlineformset_factory(
            Dados, Filho, form=FilhoForm, extra=1
        )
        form_filho = form_filho_factory(instance=dados_filho)


        form_familiares_factory = inlineformset_factory(
            Candidato, Familiares, form=FamiliaresForm, extra=1
        )
        form_familiares = form_familiares_factory(instance=dados)
            
        context = {
            "form_familiares": form_familiares,
            "pagination": pagination,
            "to_page": to_page,
            "form_dados_filho": form_dados_filho,
            "form_filho": form_filho,
            "objeto": objeto,
        }
        return render(request, "familiares.html", context)

@login_required(login_url="/login")
def familiares_enviado(request, candidato_id):
    if request.method == "POST":
        objeto = Dados.objects.filter(user=request.user).first()
        pagination = Pagination.objects.filter(user=request.user).first()
        to_page = Candidato.objects.filter(user=request.user).first()
        objeto = Candidato.objects.filter(id=candidato_id).first()
        dados_filho = Dados.objects.filter(user=request.user).first()

        form_dados_filho = DadosFilhoForm(request.POST, instance=dados_filho)

        form_familiares_factory = inlineformset_factory(Candidato, Familiares, form=FamiliaresForm)
        form_familiares = form_familiares_factory(request.POST, instance=objeto)

        form_filho_factory = inlineformset_factory(Dados, Filho, form=FilhoForm)
        form_filho = form_filho_factory(request.POST, instance=dados_filho)

        if form_dados_filho.is_valid() and form_familiares.is_valid() and form_filho.is_valid():
            form_dados_filho.save()

            form_familiares.instance = objeto
            form_familiares.save()
            
            form_filho.instance = dados_filho
            form_filho.save()

            pagination.page_6 = "used"
            pagination.save()
            return redirect("formulario:formulario_conjuge_familia")
        else:
            pagination.page_6 = "active"
            pagination.save()
            # Se os formulários não forem válidos, renderize a página com os formulários e erros
            return render(request, "familiares.html", locals())
