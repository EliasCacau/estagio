from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from formulario.forms import DadosCandidatoForm, TelefoneForm
from formulario.models import DadosCandidato, Telefone


def lista(request):
    if request.method == "GET":
        dados_candidato = DadosCandidato.objects.all()
        context = {
            "lista": dados_candidato,
        }
        return render(request, "listar_dados_candidato.html", context)


def inserir(request):
    if request.method == "GET":
        form = DadosCandidatoForm()
        form_telefone_factory = inlineformset_factory(
            DadosCandidato, Telefone, form=TelefoneForm, extra=3
        )
        form_telefone = form_telefone_factory()
        context = {
            "form": form,
            "form_telefone": form_telefone,
        }
        return render(request, "dados_candidato.html", context)
    elif request.method == "POST":
        form = DadosCandidatoForm(request.POST)
        form_telefone_factory = inlineformset_factory(
            DadosCandidato, Telefone, form=TelefoneForm
        )
        form_telefone = form_telefone_factory(request.POST)
        if form.is_valid() and form_telefone.is_valid():
            dados_candidato = form.save()
            form_telefone.instance = dados_candidato
            form_telefone.save()
            return redirect(reverse("formulario:inlineform_lista"))
        else:
            context = {
                "form_telefone": form_telefone,
                "form": form,
            }
            return render(request, "listar_dados_candidato.html", context)


def editar(request, dados_candidato_id):
    if request.method == "GET":
        objeto = DadosCandidato.objects.filter(id=dados_candidato_id).first()
        if objeto is None:
            return redirect(reverse("inlineform_lista"))
        form = DadosCandidatoForm(instance=objeto)
        form_telefone_factory = inlineformset_factory(
            DadosCandidato, Telefone, form=TelefoneForm, extra=1
        )
        form_telefone = form_telefone_factory(instance=objeto)
        context = {"form_telefone": form_telefone, "form": form}
        return render(request, "dados_candidato.html", context)
    elif request.method == "POST":
        objeto = DadosCandidato.objects.filter(id=dados_candidato_id).first()
        if objeto is None:
            return redirect(reverse("inlineform_lista"))
        form = DadosCandidatoForm(request.POST, instance=objeto)
        form_telefone_factory = inlineformset_factory(
            DadosCandidato, Telefone, form=TelefoneForm
        )
        form_telefone = form_telefone_factory(request.POST, instance=objeto)
        # if form.is_valid() and form_telefone.is_valid():
        if form_telefone.is_valid():
            # dados_candidato = form.save()
            form_telefone.instance = form
            form_telefone.save()
            return redirect(reverse("formulario:inlineform_lista"))
        else:
            context = {
                "form_telefone": form_telefone,
            }
            return render(request, "dados_candidato.html", context)
