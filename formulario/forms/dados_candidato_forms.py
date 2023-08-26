# forms.py
# flake8: noqa
import datetime
import re

from django import forms
from django.core.exceptions import ValidationError

from ..models.dados_candidato_models import DadosCandidato

OPCOES = [
    ("Solteiro", "Solteiro"),
    ("Casado", "Casado"),
    ("Divorciado", "Divorciado"),
    ("Viúvo", "Viúvo"),
]


class DadosCandidatoForm(forms.ModelForm):
    class Meta:
        model = DadosCandidato
        fields = [
            "nome_candidato",
            "data_nasc_candidato",
            "estado_civil",
            "apelido_candidato",
            "nacionalidade",
            "natural",
            "uf_natural",
            "nome_pai",
            "nome_mae",
            "idiomas",
            "num_identidade",
            "orgao_emissor",
            "num_titulo_eleitor",
            "zona_titulo",
            "num_carteira_profissional",
            "serie_carteira_prof",
        ]

        labels = {
            "nome_candidato": "Nome do Candidato",
            "data_nasc_candidato": "Data de Nascimento",
            "estado_civil": "Estado Civil",
            "apelido_candidato": "Apelido Candidato",
            "nacionalidade": "Nacionalidade",
            "natural": "Natural",
            "uf_natural": "Estado Naturalidade",
            "nome_pai": "Nome do Pai",
            "nome_mae": "Nome da Mãe",
            "idiomas": "Idiomas Falantes",
            "num_identidade": "Número da Identidade",
            "orgao_emissor": "Orgão Emissor",
            "num_titulo_eleitor": "Número do Título de Eleitor",
            "zona_titulo": "Zona do Título de Eleitor",
            "num_carteira_profissional": "Número da Carteira Profissional",
            "serie_carteira_prof": "Série da Carteira Profissional",
        }

        label_attr = {"nome_candidato": {"for": "floatingInputValue"}}

        widgets = {
            "nome_candidato": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "floatingInputValue",
                    "placeholder": "Nome Completo",
                }
            ),
            "data_nasc_candidato": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "estado_civil": forms.Select(attrs={"class": "form-select"}),
            "apelido_candidato": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apelido"}
            ),
            "nacionalidade": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nacionalidade"}
            ),
            "natural": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Naturalidade"}
            ),
            "uf_natural": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Estado Naturalidade"}
            ),
            "nome_pai": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome Pai"}
            ),
            "nome_mae": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome Mãe"}
            ),
            "idiomas": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Idiomas Falantes"}
            ),
            "num_identidade": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: 999999-9",
                }
            ),
            "orgao_emissor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Orgão Emissor Ex.: PC-AC",
                }
            ),
            "num_titulo_eleitor": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "N° Titulo Eleitor"}
            ),
            "zona_titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Zona do Titulo Eleitor"}
            ),
            "num_carteira_profissional": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "N° Carteira Profissional",
                }
            ),
            "serie_carteira_prof": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Série Carteira Prof.",
                }
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
            "estado_civil": {
                "required": "Selecione uma opção",
            },
            "apelido_candidato": {
                "required": 'Campo "Apelido Candidato" obrigatório',
            },
            "nacionalidade": {
                "required": 'Campo "Nacionalidade" obrigatório',
            },
            "natural": {
                "required": 'Campo "Natural" Obrigatório',
            },
            "uf_natural": {
                "required": 'Campo "Estado Naturalidade" Obrigatório',
            },
            "nome_pai": {
                "required": 'Campo "Nome do Pai" Obrigatório',
            },
            "nome_mae": {
                "required": 'Campo "Nome da Mãe" Obrigatório',
            },
            "idiomas": {
                "required": 'Campo "Idiomas Falantes" Obrigatório',
            },
            "num_identidade": {
                "required": 'Campo "Número da Identidade" Obrigatório',
            },
            "orgao_emissor": {
                "required": 'Campo "Orgão Emissor" Obrigatório',
            },
            "num_titulo_eleitor": {
                "required": 'Campo "Número do Título de Eleitor" Obrigatório',
            },
            "zona_titulo": {
                "required": 'Campo "Zona do Título de Eleitor" Obrigatório',
            },
            "num_carteira_profissional": {
                "required": 'Campo "Número da Carteira Profissional" Obrigatório',
            },
            "serie_carteira_prof": {
                "required": 'Campo "Série da Carteira Profissional" Obrigatório',
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
