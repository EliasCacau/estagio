# forms.py
# flake8: noqa
import datetime
import re

from django import forms
from django.core.exceptions import ValidationError

from ..models.dados_candidato_models import DadosCandidato, DadosCandidato2

# def add_attr(field, attr_name, attr_new_val):
#     existing_attr = field.widget.attrs.get(attr_name, "")
#     field.widget.attrs[attr_name] = f"{existing_attr} {attr_new_val}".strip()


# def add_placehloder(field, placeholder_val):
#     add_attr(field, "placeholder", placeholder_val)


class DadosCandidatoForm(forms.ModelForm):
    class Meta:
        model = DadosCandidato
        fields = ["nome_candidato", "data_nasc_candidato"]

        labels = {
            "nome_candidato": "Nome do Candidato",
            "data_nasc_candidato": "Data de Nascimento",
        }
        widgets = {
            "nome_candidato": forms.TextInput(
                attrs={"class": "form-control col-md-6", "placeholder": "Nome Completo"}
            ),
            "data_nasc_candidato": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
        help_text = {"nome_candidato": "Digite o nome completo"}
        error_messages = {
            "nome_candidato": {
                "required": "Insira o nome do candidato",
            },
            "data_nasc_candidato": {
                "required": "Insira a data de nascimento",
                "invalid": "Este campo é inválido",
            },
        }

    # def clean(self):  # valida todo o formulario
    # cleaned_data = super().clean()
    # nome = cleaned_data.get("nome_candidato")

    def clean_data_nasc_candidato(self):
        try:
            # Tenta converter a string em uma data válida
            data_nasc_candidato = self.cleaned_data.get("data_nasc_candidato")

            data_nasc_candidato_datetime = datetime.datetime(
                year=data_nasc_candidato.year,
                month=data_nasc_candidato.month,
                day=data_nasc_candidato.day,
            )

            # Verifica se a data está dentro de um intervalo razoável
            data_atual = datetime.datetime.now()
            idade_minima = 18  # Por exemplo, você pode definir a idade mínima desejada
            idade_maxima = 120  # E a idade máxima razoável
            idade = (data_atual - data_nasc_candidato_datetime).days // 365

            if idade < idade_minima or idade > idade_maxima:
                raise ValidationError("Data de nascimento inválida")
            return data_nasc_candidato

        except ValueError:
            raise ValidationError("Data de nascimento inválida")

    def clean_nome_candidato(self):  # validaespecifico do campo
        regex = re.compile(r"^[a-zA-ZÀ-ÿ\s]+ [a-zA-ZÀ-ÿ\s]+$")
        nome_candidato = self.cleaned_data.get("nome_candidato")

        if not regex.match(nome_candidato):
            raise ValidationError("Insira um nome válido", code="invalid")
        return nome_candidato


class RegisterForm2(forms.ModelForm):
    class Meta:
        model = DadosCandidato2
        fields = "__all__"
        errors = {"nome_candidato": "Insira o nome do candidato"}
        labels = {
            "nome_candidato": "Nome do Candidato",
            "data_nasc_candidato": "Data de Nascimento",
        }
        widgets = {
            "nome_candidato": forms.TextInput(
                attrs={"class": "form-control col-md-6", "placeholder": "Nome Completo"}
            ),
            "data_nasc_candidato": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "apelido_candidato": forms.TextInput(attrs={"class": "form-control"}),
            "nacionalidade": forms.TextInput(attrs={"class": "form-control"}),
            "natural": forms.TextInput(attrs={"class": "form-control"}),
            "uf_natural": forms.TextInput(attrs={"class": "form-control"}),
        }
        help_text = {"nome_candidato": "Digite o nome completo"}
