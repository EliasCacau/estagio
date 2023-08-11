# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import DadosCandidato


def validate_not_empty(value):
    if not value.strip():
        raise ValidationError("Este campo não pode estar vazio.")


class RegisterForm(forms.ModelForm):
    class Meta:
        model = DadosCandidato
        fields = ["nome_candidato", "data_nasc_candidato"]
        errors = {"nome_candidato": "Insira o nome do candidato"}
        validators = RegexValidator(
            regex="^[A-Za-z]*$", message="Informe apenas letras.", code="invalid_nome"
        )
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


class RegisterForm2(forms.ModelForm):
    class Meta:
        model = DadosCandidato
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
